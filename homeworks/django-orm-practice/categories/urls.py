from django.urls import path
from .views import add_category, cat_details, category_home

urlpatterns = [
    path("", category_home, name="category_home"),
    path("/add", add_category, name="add_category"),
    path("/<int:id>", cat_details, name="category_details")
]