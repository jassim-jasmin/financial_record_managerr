#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Mohammed Jassim at 19/09/25
from pydantic import BaseModel
from typing import Optional, Dict
from datetime import datetime
from app.models.budget import PeriodType, Budget

class BudgetCreate(BaseModel):
    name: str
    amount: float
    currency: Optional[str] = "USD"
    period_type: PeriodType
    period_start: datetime
    period_end: datetime
    categories: Dict[str, float] = {}
    rollover: bool = False
    alert_threshold: float = 0.8

class BudgetUpdate(BaseModel):
    name: Optional[str] = None
    amount: Optional[float] = None
    categories: Optional[Dict[str, float]] = None
    rollover: Optional[bool] = None
    alert_threshold: Optional[float] = None

class BudgetResponse(Budget):
    pass

class BudgetProgress(BaseModel):
    budget_id: str
    spent: float
    remaining: float
    percentage: float