#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Mohammed Jassim at 19/09/25
from pydantic_settings import BaseSettings
from typing import List
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    DATABASE_TYPE: str = "json"  # json or mongodb
    MONGODB_URL: str = "mongodb://localhost:27017/financial_db"
    JWT_SECRET_KEY: str = "your-super-secret-jwt-key-change-in-prod"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRE_MINUTES: int = 30
    REFRESH_EXPIRE_MINUTES: int = 1440
    DEBUG: bool = True
    DATA_DIR: str = "data"
    LOG_DIR: str = "logs"
    BASE_CURRENCY: str = "USD"
    FEATURE_2FA_ENABLED: bool = False
    FEATURE_CURRENCY_AUTO_UPDATE: bool = True
    FEATURE_REAL_TIME_NOTIFICATIONS: bool = True
    FEATURE_BUDGET_ALERTS: bool = True
    CORS_ORIGINS: List[str] = ["*"]

    class Config:
        env_file = ".env"

settings = Settings()