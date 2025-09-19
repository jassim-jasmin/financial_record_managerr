#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Mohammed Jassim at 19/09/25
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from app.services.auth_service import AuthService
from app.schemas.user_schemas import UserCreate, UserLogin, Token
from app.utils.security import get_current_user
from app.database import get_repository

router = APIRouter()
repo = get_repository()
auth_service = AuthService(repo)

@router.post("/register", response_model=UserResponse)
async def register(user: UserCreate):
    db_user = await auth_service.register(user)
    return db_user

@router.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    tokens = await auth_service.login(form_data.username, form_data.password)
    if not tokens:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return tokens

@router.post("/refresh", response_model=Token)
async def refresh(refresh_token: str):
    token = await auth_service.refresh(refresh_token)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid refresh token")
    return token

@router.post("/logout")
async def logout(token: str = Depends(get_current_user)):
    await auth_service.logout(token)
    return {"message": "Logged out"}

# 2FA endpoints (if enabled)
if settings.FEATURE_2FA_ENABLED:
    @router.post("/enable-2fa")
    async def enable_2fa(current_user: User = Depends(get_current_user)):
        secret = await auth_service.enable_2fa(current_user.id)
        return {"secret": secret}

    @router.post("/verify-2fa")
    async def verify_2fa(totp: str, current_user: User = Depends(get_current_user)):
        success = await auth_service.verify_2fa(current_user.id, totp)
        if not success:
            raise HTTPException(status_code=400, detail="Invalid TOTP")
        return {"message": "2FA verified"}

# Forgot/Reset password (simplified)
@router.post("/forgot-password")
async def forgot_password(email: str):
    await auth_service.forgot_password(email)
    return {"message": "Reset email sent"}

@router.post("/reset-password")
async def reset_password(token: str, new_password: str):
    success = await auth_service.reset_password(token, new_password)
    if not success:
        raise HTTPException(status_code=400, detail="Invalid reset token")
    return {"message": "Password reset"}