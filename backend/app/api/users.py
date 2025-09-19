#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Mohammed Jassim at 19/09/25
from fastapi import APIRouter, Depends, HTTPException
from app.services.auth_service import AuthService
from app.utils.security import get_current_user
from app.database import get_repository
from app.models.user import User
from app.schemas.user_schemas import UserResponse

router = APIRouter()
repo = get_repository()
auth_service = AuthService(repo)

@router.get("/profile", response_model=UserResponse)
async def get_profile(current_user: User = Depends(get_current_user)):
    return current_user

@router.put("/profile", response_model=UserResponse)
async def update_profile(update_data: dict, current_user: User = Depends(get_current_user)):
    updated = await auth_service.update_profile(current_user.id, update_data)
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return updated

@router.get("/search")
async def search_users(query: str, current_user: User = Depends(get_current_user)):
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Admin only")
    users = await auth_service.search_users(query)
    return users