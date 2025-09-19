#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Mohammed Jassim at 19/09/25
import asyncio
from fastapi import WebSocket
from typing import Dict, List
from app.utils.logger import logger

class NotificationService:
    def __init__(self):
        self.active_connections: Dict[str, List[WebSocket]] = {}

    async def connect(self, websocket: WebSocket, user_id: str):
        await websocket.accept()
        if user_id not in self.active_connections:
            self.active_connections[user_id] = []
        self.active_connections[user_id].append(websocket)

    def disconnect(self, websocket: WebSocket, user_id: str):
        if user_id in self.active_connections:
            self.active_connections[user_id].remove(websocket)

    async def notify(self, user_id: str, message: Dict):
        if user_id in self.active_connections:
            disconnected = []
            for connection in self.active_connections[user_id]:
                try:
                    await connection.send_json(message)
                except Exception:
                    disconnected.append(connection)
            for conn in disconnected:
                self.active_connections[user_id].remove(conn)
            if not self.active_connections[user_id]:
                del self.active_connections[user_id]

    async def notify_budget_alert(self, user_id: str, budget_id: str):
        message = {"type": "budget_alert", "budget_id": budget_id, "message": "Budget threshold exceeded"}
        await self.notify(user_id, message)

notification_service = NotificationService()

# WebSocket endpoint (add to main.py or separate router)
from fastapi import WebSocket, WebSocketDisconnect

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket, token: str = Depends(get_current_user)):
    user = await get_user_from_token(token)  # Implement
    await notification_service.connect(websocket, user.id)
    try:
        while True:
            data = await websocket.receive_text()
    except WebSocketDisconnect:
        notification_service.disconnect(websocket, user.id)