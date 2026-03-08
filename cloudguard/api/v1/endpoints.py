from ninja import Router
from typing import List
from core.models import K8sCluster
from .schemas import K8sClusterSchema

router = Router()

@router.get("/clusters", response=List[K8sClusterSchema])
def list_clusters(request):
    return K8sCluster.objects.all()