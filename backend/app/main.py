#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Mohammed Jassim at 19/09/25
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

from app.config import settings
from app.middleware.cors import cors_origins
from app.middleware.logging import LoggingMiddleware
from app.api import auth, users, financial_records, budgets, sharing
from app.utils.logger import logger

limiter = Limiter(key_func=get_remote_address)
app = FastAPI(title="Financial Management System", version="1.0.0")

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(LoggingMiddleware)

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(financial_records.router, prefix="/records", tags=["financial_records"])
app.include_router(budgets.router, prefix="/budgets", tags=["budgets"])
app.include_router(sharing.router, prefix="/sharing", tags=["sharing"])


@app.get("/")
async def root():
    return {"message": "Financial Management System API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
