from django.urls import path
from .views import ProductoCreate, CategoriaCreate, ProductoList, ProductoDelete, ProductoUpdate, ProductoDetail

app_name = "producto"

urlpatterns = [
    path("producto/list/", ProductoList.as_view(), name="producto_list"),
    path("producto/create/", ProductoCreate.as_view(), name="producto_create"),
    path("producto/categoriacreate/", CategoriaCreate.as_view(), name="categoria_create"),
    path("producto/delete/<int:pk>", ProductoDelete.as_view(), name="producto_delete"),
    path("producto/update/<int:pk>", ProductoUpdate.as_view(), name="producto_update"),
    path("producto/detail/<int:pk>", ProductoDetail.as_view(), name="producto_detail"),
]