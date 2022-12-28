from django.urls import path, include
from .views import (
    ProductView, UserView, FavoriteView, VoucherView
)

urlpatterns = [
    path("product", ProductView.as_view()),
    path("user", UserView.as_view()),
    path("favorite", FavoriteView.as_view(http_method_names=["post"])),
    path("favorite/<str:hash>", FavoriteView.as_view(http_method_names=["get"])),
    path("voucher/<str:code>", VoucherView.as_view()),
]  