from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from math import ceil
from .models import Product


def index(request):
    return render(request, "shop/basic.html")


def productview(request):
    products = Product.objects.all()
    print(products)
    n = len(products)
    nslides = n//4 + ceil((n/4) - (n//4))
    params = {'no_of_slides': nslides, 'range': range(nslides), 'product': products }
    return render(request, "shop/index.html", params)

def about(request):
    return render(request, "shop/about.html")


def search(request):
    return render(request, "shop/search.html")


def contact(request):
    return render(request, "shop/contact.html")


def tracker(request):
    return render(request, "shop/tracker.html")


def checkout(request):
    return render(request, "shop/checkout.html")


