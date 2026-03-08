from ninja import Schema
from datetime import datetime
from typing import Optional

class ClusterIn(Schema):
    """Dados para criar um novo cluster"""
    name: str
    api_endpoint: str
    provider_info: dict = {}

class ClusterOut(Schema):
    """Dados que a API retorna (com ID e Datas)"""
    id: int
    name: str
    api_endpoint: str
    provider_info: dict
    is_active: bool
    created_at: datetime