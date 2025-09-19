#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Mohammed Jassim at 19/09/25
from pydantic import BaseModel, Field
from typing import Optional, Dict, List
from datetime import datetime
from enum import Enum

class PeriodType(str, Enum):
    MONTHLY = "monthly"
    YEARLY = "yearly"

class Budget(BaseModel):
    id: str
    name: str
    amount: float
    currency: str = "USD"
    period_type: PeriodType
    period_start: datetime
    period_end: datetime
    categories: Dict[str, float] = {}  # category: allocated_amount
    user_id: str
    rollover: bool = False
    alert_threshold: float = 0.8  # 80% threshold
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)