from django.urls import path
from . import views

urlpatterns = [
    # path("products_all", views.products_all_DEF, name="products_all-URL"),
    path("checkout/", views.checkout_DEF, name="checkout-URL"),
]  