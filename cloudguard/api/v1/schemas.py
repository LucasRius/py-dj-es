from ninja import Schema
from datetime import datetime

class K8sClusterSchema(Schema):
    id: int
    name: str
    api_endpoint: str
    created_at: datetime