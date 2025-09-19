#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Mohammed Jassim at 19/09/25
from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import datetime

class User(BaseModel):
    id: str
    email: EmailStr
    hashed_password: str
    full_name: Optional[str] = None
    is_active: bool = True
    is_admin: bool = False
    two_factor_secret: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class Permission(BaseModel):
    id: str
    user_id: str
    resource_type: str  # e.g., 'record', 'budget'
    resource_id: str
    permission_level: str  # 'read', 'write', 'admin'
    granted_by: str
    created_at: datetime = Field(default_factory=datetime.utcnow)