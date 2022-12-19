from django.urls import path, include
from .views import (
    AddProduct,
)

urlpatterns = [
    path("product/add", AddProduct.as_view()),
]  