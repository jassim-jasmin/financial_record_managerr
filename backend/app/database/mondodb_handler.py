#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Mohammed Jassim at 19/09/25
from typing import Dict, Any, List, Optional
from motor.motor_asyncio import AsyncIOMotorClient
from app.config import settings
from app.database.base_repository import BaseRepository
from app.utils.logger import logger

class MongoRepository(BaseRepository):
    def __init__(self):
        self.client = AsyncIOMotorClient(settings.MONGODB_URL)
        self.db = self.client[settings.MONGODB_URL.split('/')[-1].split('?')[0]]

    async def create(self, collection: str, data: Dict[str, Any]) -> Dict[str, Any]:
        result = await self.db[collection].insert_one(data)
        data["_id"] = str(result.inserted_id)
        return data

    async def read(self, collection: str, id: str) -> Optional[Dict[str, Any]]:
        return await self.db[collection].find_one({"_id": id})

    async def update(self, collection: str, id: str, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        result = await self.db[collection].update_one(
            {"_id": id},
            {"$set": data}
        )
        if result.modified_count > 0:
            data["_id"] = id
            return data
        return None

    async def delete(self, collection: str, id: str) -> bool:
        result = await self.db[collection].delete_one({"_id": id})
        return result.deleted_count > 0

    async def list(self, collection: str, filters: Dict[str, Any] = None) -> List[Dict[str, Any]]:
        query = filters or {}
        cursor = self.db[collection].find(query)
        return await cursor.to_list(length=None)