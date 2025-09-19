#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Mohammed Jassim at 19/09/25
from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional

class BaseRepository(ABC):
    @abstractmethod
    async def create(self, collection: str, data: Dict[str, Any]) -> Dict[str, Any]:
        pass

    @abstractmethod
    async def read(self, collection: str, id: str) -> Optional[Dict[str, Any]]:
        pass

    @abstractmethod
    async def update(self, collection: str, id: str, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        pass

    @abstractmethod
    async def delete(self, collection: str, id: str) -> bool:
        pass

    @abstractmethod
    async def list(self, collection: str, filters: Dict[str, Any] = None) -> List[Dict[str, Any]]:
        pass