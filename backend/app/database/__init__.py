#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Mohammed Jassim at 19/09/25
from .base_repository import BaseRepository
from .json_handler import JSONRepository
from .mongodb_handler import MongoRepository

def get_repository(db_type: str = None):
    db_type = db_type or settings.DATABASE_TYPE
    if db_type == "json":
        return JSONRepository()
    elif db_type == "mongodb":
        return MongoRepository()
    else:
        raise ValueError(f"Unsupported database type: {db_type}")