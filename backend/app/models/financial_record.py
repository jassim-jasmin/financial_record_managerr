#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Mohammed Jassim at 19/09/25
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from datetime import datetime
from enum import Enum

class RecordType(str, Enum):
    EXPENSE = "expense"
    INCOME = "income"
    TRANSFER = "transfer"

class FinancialRecord(BaseModel):
    id: str
    type: RecordType
    amount: float
    currency: str = "USD"
    description: Optional[str] = None
    date: datetime
    category: Optional[str] = None
    user_id: str
    from_user: Optional[str] = None  # For transfers
    to_user: Optional[str] = None    # For transfers
    custom_fields: Dict[str, Any] = {}
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)