from fastapi import APIRouter
from services.operadora import list_operadoras, list_operadoras_by_field, list_fields, list_distinct_field_values
from typing import  Any
from fastapi.responses import JSONResponse
from typings.operadora import Operadora
from datetime import datetime

router = APIRouter(
    prefix="/operadoras",
    tags=["Operadoras"],
)

@router.get("/")
def get_operadoras():
    return JSONResponse(list_operadoras())

@router.get("/fields", response_model=list[str])
def get_fields():
    return JSONResponse(list_fields())

@router.get("/query/{field}={value}")
def get_operadora_by_field(field: str, value: Any):
    columns = list_fields()
    key = field.upper()
    if key not in columns:
        return {"error": "Invalid field", "message": "Please, check /fields endpoint" , "status": 400}
    
    return JSONResponse(list_operadoras_by_field(field, value))

@router.get("/distinct/{field}")
def get_distinct_field_values(field: str):
    columns = list_fields()
    key = field.upper()
    if key not in columns:
        return {"error": "Invalid field", "message": "Please, check /fields endpoint" , "status": 400,
                "teste": f"field: {field}, field type: {type(field)}"}
    return JSONResponse(list_distinct_field_values(key))