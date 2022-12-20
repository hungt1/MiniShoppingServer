from django.urls import path, include
from .views import (
    AddProduct,
    AddUser,
    AddFollowings,
    GetProductsQuery,
    GetProduct
)

urlpatterns = [
    path("product/add", AddProduct.as_view()),
    path("product", GetProductsQuery.as_view()),
    path("product/<int:product_id>", GetProduct.as_view()),
]  