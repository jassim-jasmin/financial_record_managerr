#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Mohammed Jassim at 19/09/25
from pydantic import validator, ValidationError
from datetime import datetime
from decimal import Decimal

def validate_amount(cls, v):
    if v <= 0:
        raise ValueError("Amount must be positive")
    return Decimal(str(v)).quantize(Decimal('0.01'))

def validate_date(cls, v):
    if v > datetime.utcnow():
        raise ValueError("Date cannot be in the future for expenses")
    return v

# Use in schemas with @validator