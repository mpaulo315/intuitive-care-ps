from pydantic import BaseModel
from typing import Optional
from datetime import date

class Operadora(BaseModel):
    id: int
    cnpj: str
    razao_social: str
    nome_fantasia: Optional[str]
    modalidade: str
    logradouro: str
    numero: Optional[str | int]
    complemento: Optional[str]
    bairro: str
    cidade: str
    uf: str
    cep: str
    ddd: Optional[str]
    telefone: Optional[str]
    fax: Optional[str]
    email: Optional[str]
    representante: str
    cargo_representante: str
    regiao_comercial: Optional[int]
    data_registro_ans: date

