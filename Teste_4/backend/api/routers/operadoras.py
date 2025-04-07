from fastapi import APIRouter, HTTPException
from services.operadora import list_operadoras, list_operadoras_by_field, list_fields, list_distinct_field_values
from typing import  Any
from fastapi.responses import JSONResponse

router = APIRouter(
    prefix="/operadoras",
    tags=["Operadoras"],
)

@router.get("/")
def read_operadoras():
    return JSONResponse(list_operadoras())

@router.get("/fields", response_model=list[str])
def read_fields():
    return JSONResponse(list_fields())

@router.get("/query/{field}={value}")
def read_operadora_by_field(field: str, value: Any):
    columns = list_fields()
    key = field.upper()
    if key not in columns:
        raise HTTPException(status_code=400, detail="Invalid field. Please, check /fields endpoint")    
    return JSONResponse(list_operadoras_by_field(field, value))

@router.get("/{field}/distinct")
def read_distinct_field_values(field: str):
    columns = list_fields()
    key = field.upper()
    if key not in columns:
        raise HTTPException(status_code=400, detail="Invalid field. Please, check /fields endpoint")
    return JSONResponse(list_distinct_field_values(key))