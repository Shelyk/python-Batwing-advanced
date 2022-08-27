
from django.shortcuts import render, redirect, get_object_or_404

from main.models import MenuItem
from products.models import Product
from .models import Category

def category_home(request):

    menu_items = MenuItem.objects.filter(url__startswith='/categories').order_by('-name')
    categories = Category.objects.order_by("cat_title")
    products = Product.objects.order_by("title")

    return render(request, 'categories/cat_main.html', {
        "menu_items": menu_items,
        "categories": categories,
        "products": products
    })


def add_category(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            return render(request, "categories/add.html")
        else:
            category = Category()
            category.cat_title = request.POST.get("cat_title")
            category.description = request.POST.get("description")
            category.save()
            return redirect("/")
    else:
        return redirect("/")


def cat_details(request, id):
    category = get_object_or_404(Category, id=id)
    return render(request, "categories/cat_details.html", {"category": category})