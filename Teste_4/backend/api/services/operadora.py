from repositories.operadoras import get_operadoras, get_distinct_field_values, get_operadoras_by_field, get_fields
from typings.operadora import Operadora

def list_operadoras() -> list[Operadora]:
    return get_operadoras()

def list_operadoras_by_field(field: str, value: any) -> list[Operadora]:
    return get_operadoras_by_field(field, value)

def list_distinct_field_values(field: str) -> list[str]:
    return get_distinct_field_values(field)

def list_fields() -> list[str]:
    return get_fields()