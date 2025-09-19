#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Mohammed Jassim at 19/09/25
from typing import Dict, Any, List, Optional
from app.database.base_repository import BaseRepository
from app.models.user import User
from app.models.budget import Budget
from app.schemas.budget_schemas import BudgetCreate, BudgetUpdate, BudgetProgress
from app.services.financial_service import FinancialService
from app.utils.logger import logger

class BudgetService:
    def __init__(self, repo: BaseRepository):
        self.repo = repo
        self.financial_service = FinancialService(repo)

    async def create_budget(self, data: Dict[str, Any]) -> Budget:
        created = await self.repo.create("budgets", data)
        return Budget(**created)

    async def list_budgets(self, user_id: str) -> List[Budget]:
        filters = {"user_id": user_id}
        budgets = await self.repo.list("budgets", filters)
        return [Budget(**b) for b in budgets]

    async def update_budget(self, id: str, data: Dict[str, Any], user_id: str) -> Optional[Budget]:
        filters = {"id": id, "user_id": user_id}
        existing = await self.repo.list("budgets", filters)
        if not existing:
            return None
        return await self.repo.update("budgets", id, data)

    async def delete_budget(self, id: str, user_id: str) -> bool:
        filters = {"id": id, "user_id": user_id}
        existing = await self.repo.list("budgets", filters)
        if not existing:
            return False
        return await self.repo.delete("budgets", id)

    async def get_progress(self, budget_id: str, user_id: str) -> Optional[BudgetProgress]:
        budget_data = await self.repo.read("budgets", budget_id)
        if not budget_data or budget_data["user_id"] != user_id:
            return None
        budget = Budget(**budget_data)
        # Get expenses in period for categories
        filters = {
            "user_id": user_id,
            "type": "expense",
            "date": {"$gte": budget.period_start, "$lte": budget.period_end}  # Adapt for JSON
        }
        records = await self.financial_service.list_records(filters)
        spent = sum(r.amount for r in records if r.category in budget.categories)
        remaining = budget.amount - spent
        percentage = spent / budget.amount if budget.amount > 0 else 0
        return BudgetProgress(budget_id=budget_id, spent=spent, remaining=remaining, percentage=percentage)

    async def get_analytics(self, budget_id: str, user_id: str) -> Dict:
        progress = await self.get_progress(budget_id, user_id)
        if not progress:
            return {}
        # More detailed analytics
        return {"progress": progress.dict()}
