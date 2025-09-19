#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Mohammed Jassim at 19/09/25
from datetime import timedelta, datetime
from typing import Optional
from jose import JWTError, jwt
from passlib.context import CryptContext
from app.config import settings
from app.database.base_repository import BaseRepository
from app.models.user import User, Permission
from app.schemas.user_schemas import UserCreate, Token
from app.utils.security import verify_password, get_password_hash, create_access_token, create_refresh_token
from app.utils.logger import logger
import pyotp

class AuthService:
    def __init__(self, repo: BaseRepository):
        self.repo = repo
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    async def register(self, user: UserCreate) -> User:
        existing = await self.repo.list("users", {"email": user.email})
        if existing:
            raise ValueError("User already exists")
        hashed = get_password_hash(user.password)
        user_data = {
            "email": user.email,
            "hashed_password": hashed,
            "full_name": user.full_name,
        }
        created = await self.repo.create("users", user_data)
        return User(**created)

    async def login(self, email: str, password: str) -> Optional[Token]:
        user_data = await self.repo.list("users", {"email": email})
        if not user_data or not verify_password(password, user_data[0]["hashed_password"]):
            return None
        user = User(**user_data[0])
        if not user.is_active:
            return None
        access = create_access_token(data={"sub": user.email, "id": user.id}, expires_delta=timedelta(minutes=settings.JWT_EXPIRE_MINUTES))
        refresh = create_refresh_token(data={"sub": user.email}, expires_delta=timedelta(minutes=settings.REFRESH_EXPIRE_MINUTES))
        return Token(access_token=access, refresh_token=refresh)

    async def refresh(self, refresh_token: str) -> Optional[Token]:
        try:
            payload = jwt.decode(refresh_token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
            email: str = payload.get("sub")
            if email is None:
                return None
        except JWTError:
            return None
        user_data = await self.repo.list("users", {"email": email})
        if not user_data:
            return None
        access = create_access_token(data={"sub": email}, expires_delta=timedelta(minutes=settings.JWT_EXPIRE_MINUTES))
        new_refresh = create_refresh_token(data={"sub": email}, expires_delta=timedelta(minutes=settings.REFRESH_EXPIRE_MINUTES))
        return Token(access_token=access, refresh_token=new_refresh)

    async def logout(self, token: str):
        # In production, add to blacklist
        logger.info(f"Logout for token: {token[:10]}...")

    async def enable_2fa(self, user_id: str) -> str:
        secret = pyotp.random_base32()
        await self.repo.update("users", user_id, {"two_factor_secret": secret})
        return secret

    async def verify_2fa(self, user_id: str, totp: str) -> bool:
        user_data = await self.repo.read("users", user_id)
        if not user_data or not user_data.get("two_factor_secret"):
            return False
        totp_obj = pyotp.TOTP(user_data["two_factor_secret"])
        return totp_obj.verify(totp)

    async def forgot_password(self, email: str):
        # Send email logic (mock)
        logger.info(f"Password reset requested for {email}")

    async def reset_password(self, token: str, new_password: str) -> bool:
        # Verify token and update (mock)
        hashed = get_password_hash(new_password)
        # Find user by token, update
        return True

    async def update_profile(self, user_id: str, update_data: dict) -> Optional[User]:
        return await self.repo.update("users", user_id, update_data)

    async def search_users(self, query: str) -> list:
        filters = {"email": {"$regex": query, "$options": "i"}}  # Mongo style, adapt for JSON
        return await self.repo.list("users", filters)

    async def grant_permission(self, granter_id: str, user_email: str, resource_type: str, resource_id: str, level: str) -> Permission:
        user_data = await self.repo.list("users", {"email": user_email})
        if not user_data:
            raise ValueError("User not found")
        target_user_id = user_data[0]["id"]
        perm_data = {
            "user_id": target_user_id,
            "resource_type": resource_type,
            "resource_id": resource_id,
            "permission_level": level,
            "granted_by": granter_id,
        }
        created = await self.repo.create("permissions", perm_data)
        return Permission(**created)

    async def get_shared_resources(self, user_id: str) -> list:
        filters = {"user_id": user_id}
        perms = await self.repo.list("permissions", filters)
        # Fetch resources based on perms
        resources = []
        for perm in perms:
            if perm["resource_type"] == "record":
                record = await self.repo.read("financial_records", perm["resource_id"])
                if record:
                    resources.append(record)
            # Similar for budgets
        return resources