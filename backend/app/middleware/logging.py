#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Mohammed Jassim at 19/09/25
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from app.utils.logger import logger
import time

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        logger.info(
            "Request completed",
            method=request.method,
            url=request.url,
            status_code=response.status_code,
            process_time=process_time,
        )
        return response