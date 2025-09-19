#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Mohammed Jassim at 19/09/25
from fastapi import APIRouter, Depends
from app.services.auth_service import AuthService
from app.utils.security import get_current_user
from app.database import get_repository
from app.models.user import User, Permission
from app.schemas.user_schemas import UserResponse

router = APIRouter()
repo = get_repository()
auth_service = AuthService(repo)

@router.post("/permission")
async def share_permission(resource_type: str, resource_id: str, user_email: str, level: str, current_user: User = Depends(get_current_user)):
    permission = await auth_service.grant_permission(current_user.id, user_email, resource_type, resource_id, level)
    return permission

@router.get("/shared-with-me")
async def get_shared_resources(current_user: User = Depends(get_current_user)):
    shared = await auth_service.get_shared_resources(current_user.id)
    return shared