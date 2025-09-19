#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Mohammed Jassim at 19/09/25
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from typing import Optional
from app.services.financial_service import FinancialService
from app.utils.security import get_current_user
from app.database import get_repository
from app.models.user import User
from app.schemas.financial_schemas import (
    FinancialRecordCreate, FinancialRecordUpdate, FinancialRecordResponse, BulkImport
)
from app.models.financial_record import FinancialRecord

router = APIRouter()
repo = get_repository()
financial_service = FinancialService(repo)

@router.get("/", response_model=list[FinancialRecordResponse])
async def list_records(
    type: Optional[str] = None,
    category: Optional[str] = None,
    date_from: Optional[str] = None,
    date_to: Optional[str] = None,
    current_user: User = Depends(get_current_user)
):
    filters = {"user_id": current_user.id}
    if type:
        filters["type"] = type
    if category:
        filters["category"] = category
    # Add date filters logic here
    records = await financial_service.list_records(filters)
    return records

@router.post("/", response_model=FinancialRecordResponse)
async def create_record(record: FinancialRecordCreate, current_user: User = Depends(get_current_user)):
    record_dict = record.dict()
    record_dict["user_id"] = current_user.id
    created = await financial_service.create_record(record_dict)
    # Trigger notification if needed
    await financial_service.check_budget_alerts(created)
    return created

@router.put("/{id}", response_model=FinancialRecordResponse)
async def update_record(id: str, update: FinancialRecordUpdate, current_user: User = Depends(get_current_user)):
    updated = await financial_service.update_record(id, update.dict(), current_user.id)
    if not updated:
        raise HTTPException(status_code=404, detail="Record not found")
    return updated

@router.delete("/{id}")
async def delete_record(id: str, current_user: User = Depends(get_current_user)):
    success = await financial_service.delete_record(id, current_user.id)
    if not success:
        raise HTTPException(status_code=404, detail="Record not found")
    return {"message": "Deleted"}

@router.post("/bulk-import")
async def bulk_import(file: UploadFile = File(...), current_user: User = Depends(get_current_user)):
    # Handle CSV/Excel import using pandas
    import pandas as pd
    import io
    content = await file.read()
    if file.filename.endswith('.csv'):
        df = pd.read_csv(io.BytesIO(content))
    else:
        df = pd.read_excel(io.BytesIO(content))
    records = df.to_dict('records')
    imported = await financial_service.bulk_create(records, current_user.id)
    return {"imported": len(imported)}

@router.get("/export")
async def export_records(format: str = "csv", current_user: User = Depends(get_current_user)):
    # Similar to import, generate file
    records = await financial_service.list_records({"user_id": current_user.id})
    import pandas as pd
    df = pd.DataFrame(records)
    if format == "csv":
        return df.to_csv(index=False)
    else:
        return df.to_excel(index=False)

@router.get("/analytics")
async def get_analytics(current_user: User = Depends(get_current_user)):
    analytics = await financial_service.get_analytics(current_user.id)
    return analytics