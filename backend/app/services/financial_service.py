#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Mohammed Jassim at 19/09/25
from typing import Dict, Any, List, Optional
from app.database.base_repository import BaseRepository
from app.models.user import User
from app.models.financial_record import FinancialRecord
from app.schemas.financial_schemas import FinancialRecordCreate, FinancialRecordUpdate
from app.services.budget_service import BudgetService
from app.utils.currency import convert_currency
from app.utils.logger import logger
import pandas as pd

class FinancialService:
    def __init__(self, repo: BaseRepository):
        self.repo = repo
        self.budget_service = BudgetService(repo)

    async def create_record(self, data: Dict[str, Any]) -> FinancialRecord:
        # Handle transfer logic: create two records if transfer
        if data["type"] == "transfer":
            from_data = data.copy()
            from_data["type"] = "expense"
            from_data["user_id"] = data["from_user"]
            del from_data["from_user"]
            del from_data["to_user"]
            await self.repo.create("financial_records", from_data)

            to_data = data.copy()
            to_data["type"] = "income"
            to_data["user_id"] = data["to_user"]
            del to_data["from_user"]
            del to_data["to_user"]
            await self.repo.create("financial_records", to_data)

            data["user_id"] = data["from_user"]  # Store from perspective
        else:
            data["amount"] = convert_currency(data["amount"], data["currency"], settings.BASE_CURRENCY)

        created = await self.repo.create("financial_records", data)
        return FinancialRecord(**created)

    async def list_records(self, filters: Dict[str, Any]) -> List[FinancialRecord]:
        records = await self.repo.list("financial_records", filters)
        return [FinancialRecord(**r) for r in records]

    async def update_record(self, id: str, data: Dict[str, Any], user_id: str) -> Optional[FinancialRecord]:
        filters = {"id": id, "user_id": user_id}
        existing = await self.repo.list("financial_records", filters)
        if not existing:
            return None
        # Update currency if changed
        if "currency" in data:
            data["amount"] = convert_currency(data["amount"], data["currency"], settings.BASE_CURRENCY)
        return await self.repo.update("financial_records", id, data)

    async def delete_record(self, id: str, user_id: str) -> bool:
        filters = {"id": id, "user_id": user_id}
        existing = await self.repo.list("financial_records", filters)
        if not existing:
            return False
        return await self.repo.delete("financial_records", id)

    async def bulk_create(self, records: List[Dict], user_id: str) -> List[FinancialRecord]:
        created = []
        for rec in records:
            rec["user_id"] = user_id
            created.append(await self.create_record(rec))
        return created

    async def get_analytics(self, user_id: str) -> Dict:
        filters = {"user_id": user_id}
        records = await self.repo.list("financial_records", filters)
        df = pd.DataFrame(records)
        # Simple analytics: total income, expenses, etc.
        total_income = df[df['type'] == 'income']['amount'].sum()
        total_expense = df[df['type'] == 'expense']['amount'].sum()
        return {"total_income": total_income, "total_expense": total_expense, "net": total_income - total_expense}

    async def check_budget_alerts(self, record: FinancialRecord):
        if not settings.FEATURE_BUDGET_ALERTS or record.type != "expense":
            return
        budgets = await self.budget_service.list_budgets(record.user_id)
        for budget in budgets:
            if record.category in budget.categories and record.amount > budget.alert_threshold * budget.categories[record.category]:
                # Trigger notification
                await self.notify_budget_alert(record.user_id, budget.id)