#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Mohammed Jassim at 19/09/25
from fastapi import APIRouter, Depends, HTTPException
from app.services.budget_service import BudgetService
from app.utils.security import get_current_user
from app.database import get_repository
from app.models.user import User
from app.schemas.budget_schemas import (
    BudgetCreate, BudgetUpdate, BudgetResponse, BudgetProgress
)
from app.models.budget import Budget

router = APIRouter()
repo = get_repository()
budget_service = BudgetService(repo)

@router.get("/", response_model=list[BudgetResponse])
async def list_budgets(current_user: User = Depends(get_current_user)):
    budgets = await budget_service.list_budgets(current_user.id)
    return budgets

@router.post("/", response_model=BudgetResponse)
async def create_budget(budget: BudgetCreate, current_user: User = Depends(get_current_user)):
    budget_dict = budget.dict()
    budget_dict["user_id"] = current_user.id
    created = await budget_service.create_budget(budget_dict)
    return created

@router.put("/{id}", response_model=BudgetResponse)
async def update_budget(id: str, update: BudgetUpdate, current_user: User = Depends(get_current_user)):
    updated = await budget_service.update_budget(id, update.dict(), current_user.id)
    if not updated:
        raise HTTPException(status_code=404, detail="Budget not found")
    return updated

@router.delete("/{id}")
async def delete_budget(id: str, current_user: User = Depends(get_current_user)):
    success = await budget_service.delete_budget(id, current_user.id)
    if not success:
        raise HTTPException(status_code=404, detail="Budget not found")
    return {"message": "Deleted"}

@router.get("/{id}/progress", response_model=BudgetProgress)
async def get_budget_progress(id: str, current_user: User = Depends(get_current_user)):
    progress = await budget_service.get_progress(id, current_user.id)
    if not progress:
        raise HTTPException(status_code=404, detail="Budget not found")
    return progress

@router.get("/{id}/analytics")
async def get_budget_analytics(id: str, current_user: User = Depends(get_current_user)):
    analytics = await budget_service.get_analytics(id, current_user.id)
    if not analytics:
        raise HTTPException(status_code=404, detail="Budget not found")
    return analytics