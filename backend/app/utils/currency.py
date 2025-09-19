#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Mohammed Jassim at 19/09/25
from typing import Dict
# Mock rates since no internet
RATES: Dict[str, float] = {"USD": 1.0, "EUR": 0.92, "GBP": 0.78}  # Example

def convert_currency(amount: float, from_cur: str, to_cur: str) -> float:
    if settings.FEATURE_CURRENCY_AUTO_UPDATE:
        # In real, fetch from API
        pass
    rate_from = RATES.get(from_cur, 1.0)
    rate_to = RATES.get(to_cur, 1.0)
    return amount * (rate_to / rate_from)