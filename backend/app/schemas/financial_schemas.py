#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Mohammed Jassim at 19/09/25
from pydantic import BaseModel
from typing import Optional, Dict, Any
from datetime import datetime
from app.models.financial_record import RecordType, FinancialRecord

class FinancialRecordCreate(BaseModel):
    type: RecordType
    amount: float
    currency: Optional[str] = "USD"
    description: Optional[str] = None
    date: datetime
    category: Optional[str] = None
    from_user: Optional[str] = None
    to_user: Optional[str] = None
    custom_fields: Dict[str, Any] = {}

class FinancialRecordUpdate(BaseModel):
    amount: Optional[float] = None
    description: Optional[str] = None
    date: Optional[datetime] = None
    category: Optional[str] = None
    custom_fields: Optional[Dict[str, Any]] = None

class FinancialRecordResponse(FinancialRecord):
    pass

class BulkImport(BaseModel):
    file_type: str  # csv, excel
    data: list  # Will be handled via upload