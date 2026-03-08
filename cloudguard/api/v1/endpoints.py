from django.shortcuts import get_object_or_404
from ninja import Router
# from core.models import K8sCluster
from .schemas import ClusterIn, ClusterOut

router = Router()

# @router.post("/clusters", response={201: ClusterOut})
# def create_cluster(request, data: ClusterIn):
#     # O Django 5.2 aceita o unpacking direto do Pydantic
#     cluster = K8sCluster.objects.create(**data.dict())
#     return 201, cluster

# @router.get("/clusters", response=list[ClusterOut])
# def list_clusters(request):
#     return K8sCluster.objects.all()

# @router.get("/clusters/{cluster_id}", response=ClusterOut)
# def get_cluster(request, cluster_id: int):
#     return get_object_or_404(K8sCluster, id=cluster_id)