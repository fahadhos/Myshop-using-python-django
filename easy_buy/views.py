from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
from math import ceil
from .models import Product


def index(request):
    # allProds = []
    # catprods = Product.objects.values('category', 'id')
    # cats = {item['category'] for item in catprods}
    # for cat in cats:
    #     prod = Product.objects.filter(category=cat)
    #     n = len(prod)
    #     nSlides = n // 4 + ceil((n / 4) - (n // 4))
    #     allProds.append([prod, range(1, nSlides), nSlides])
    products = Product.objects.all()
    print(products)
    n = len(products)
    nslides = n // 4 + ceil((n / 4) - (n // 4))
    catprods = Product.objects.values('category', 'id')
    subcategory = Product.category
    productlist = Product.objects.filter(subcategory=subcategory).count()

    params = {'no_of_slides': nslides, 'range': range(nslides), 'product': products, 'count': productlist}
    # params = {'allProd': allProds}
    return render(request, "shop/index.html", params)


def product(request):
    return render(request, "shop/product.html")


#
# def shop(request):
#     return render(request, "shop/product.html")


def about(request):
    return render(request, "shop/about.html")


def detail(request, pid):
    product = Product.objects.filter(id=pid)
    return render(request, "shop/detail.html", {'product': product[0]})


def search(request):
    return render(request, "shop/search.html")


def contact(request):
    if request.method == "POST":
        print(request)
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        print(name, email, phone, subject, message)
    return render(request, "shop/contact.html")


def tracker(request):
    return render(request, "shop/tracker.html")


def checkout(request):
    return render(request, "shop/checkout.html")


def cart(request):
    return render(request, "shop/cart.html")
