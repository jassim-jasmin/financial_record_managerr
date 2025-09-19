#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Mohammed Jassim at 19/09/25
import json
import os
import asyncio
from typing import Dict, Any, List, Optional
from pathlib import Path
from app.config import settings
from app.utils.logger import logger

class JSONRepository(BaseRepository):
    def __init__(self):
        self.data_dir = Path(settings.DATA_DIR)
        self.data_dir.mkdir(exist_ok=True)
        self._lock = asyncio.Lock()
        self._index: Dict[str, Dict] = {}  # In-memory index

    async def create(self, collection: str, data: Dict[str, Any]) -> Dict[str, Any]:
        async with self._lock:
            file_path = self.data_dir / f"{collection}.json"
            items = await self._read_file(file_path)
            id_field = "id" if "id" in data else "_id"
            if id_field not in data:
                data[id_field] = str(len(items) + 1)
            items.append(data)
            await self._write_file(file_path, items)
            self._update_index(collection, data[id_field], data)
            return data

    async def read(self, collection: str, id: str) -> Optional[Dict[str, Any]]:
        async with self._lock:
            if collection in self._index and id in self._index[collection]:
                return self._index[collection][id]
            file_path = self.data_dir / f"{collection}.json"
            items = await self._read_file(file_path)
            for item in items:
                if str(item.get("id", item.get("_id"))) == id:
                    self._update_index(collection, id, item)
                    return item
            return None

    async def update(self, collection: str, id: str, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        async with self._lock:
            file_path = self.data_dir / f"{collection}.json"
            items = await self._read_file(file_path)
            for i, item in enumerate(items):
                if str(item.get("id", item.get("_id"))) == id:
                    updated = {**item, **data}
                    updated["id"] = id  # Ensure ID is preserved
                    items[i] = updated
                    await self._write_file(file_path, items)
                    self._update_index(collection, id, updated)
                    return updated
            return None

    async def delete(self, collection: str, id: str) -> bool:
        async with self._lock:
            file_path = self.data_dir / f"{collection}.json"
            items = await self._read_file(file_path)
            for i, item in enumerate(items):
                if str(item.get("id", item.get("_id"))) == id:
                    del items[i]
                    await self._write_file(file_path, items)
                    if collection in self._index:
                        self._index[collection].pop(id, None)
                    return True
            return False

    async def list(self, collection: str, filters: Dict[str, Any] = None) -> List[Dict[str, Any]]:
        async with self._lock:
            file_path = self.data_dir / f"{collection}.json"
            items = await self._read_file(file_path)
            if filters:
                items = [item for item in items if self._matches_filter(item, filters)]
            # Update index with new items
            for item in items:
                iid = str(item.get("id", item.get("_id")))
                self._update_index(collection, iid, item)
            return items

    async def _read_file(self, file_path: Path) -> List[Dict]:
        if not file_path.exists():
            return []
        with open(file_path, 'r') as f:
            return json.load(f)

    async def _write_file(self, file_path: Path, data: List[Dict]):
        # Backup
        if file_path.exists():
            backup_path = file_path.with_suffix('.json.backup')
            file_path.replace(backup_path)
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=2, default=str)

    def _update_index(self, collection: str, id: str, data: Dict):
        if collection not in self._index:
            self._index[collection] = {}
        self._index[collection][id] = data

    def _matches_filter(self, item: Dict, filters: Dict) -> bool:
        for key, value in filters.items():
            if str(item.get(key, "")) != str(value):
                return False
        return True