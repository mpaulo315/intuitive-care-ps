from typings.operadora import Operadora
from datetime import datetime
from db.connection import get_connection, dict_factory
from typing import Union

def get_operadoras() -> list[Operadora]:
    """
    Returns a list of all OPERADORAS.
    :return: A list of OPERADORAS.
    """
    conn = get_connection()
    conn.row_factory = dict_factory
    return conn.execute("SELECT * FROM OPERADORAS").fetchall()

def get_operadoras_by_field(field: str, query: any) -> list[Operadora]:
    """
    Returns a list of OPERADORAS that match the given field and query.
    :param field: The field to search for.
    :type field: str
    :param query: The value to search for.
    :type query: any
    """
    conn = get_connection()
    conn.row_factory = dict_factory
    return conn.execute(f"SELECT * FROM OPERADORAS WHERE {field} = ?", (query,)).fetchall()

def get_distinct_field_values(field: str) -> list[Union[str, datetime.date, int, float, None]]:
    """
    Returns a list of distinct values for the given field.
    :param field: The field to get distinct values for.
    :type field: str
    :return: A list of distinct values for the given field.
    """
    result = get_connection().execute(f"SELECT DISTINCT {field} FROM OPERADORAS").fetchall()
    return [row[0] for row in result]

def get_fields() -> list[str]:
    """
    Returns a list of all fields in the OPERADORA table.
    :return: A list of all fields in the OPERADORA table.
    """
    conn = get_connection()
    conn.row_factory = dict_factory
    pragma = conn.execute("PRAGMA table_info(OPERADORAS)")
    return [row["name"] for row in pragma]
