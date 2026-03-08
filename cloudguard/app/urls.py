# app/urls.py
from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from api.v1.endpoints import router as v1_router

api = NinjaAPI(title="CloudGuard API")
api.add_router("/v1", v1_router) # Apenas uma vez aqui!

urlpatterns = [
    path('admin/', admin.site.urls), # Corrigido abaixo
    path('api/', api.urls),
]