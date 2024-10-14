import stripe
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from django.shortcuts import render
import time
# Create your views here.
from math import ceil
import json
from .models import *
import logging
from django.conf import settings

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django import forms
from django.contrib.auth.forms import UserCreationForm


import stripe

# Get an instance of a logger
logger = logging.getLogger(__name__)

# def redirect_view(request):
#     response = redirect('/redirect-success/')
#     return response


stripe.api_key = 'sk_test_51JJy5WFmFwh8TmzH3cvSRJ339xeXDKiR94KfjZNMHx89TFW5LyR1wm35tcj2sD1Gro0cUN7SfJSmq0ivWqnkDRyl00K9orMF01'


def index(request):
    products = Product.objects.all()
    print(products)
    n = len(products)
    nslides = n // 4 + ceil((n / 4) - (n // 4))
    catprods = Product.objects.values('category', 'id')
    subcategory = Product.category
    productlist = Product.objects.filter(subcategory=subcategory).count()

    params = {'no_of_slides': nslides, 'range': range(nslides), 'product': products, 'count': productlist}

    return render(request, "shop/index.html", params)


def searchMatch(query, item):
    '''return true only if search matches'''
    if query in item.desc.lower() or query in item.product_name.lower() or query in item.category.lower() or query in item.category:
        return True
    else:
        return False


def Login(request):
    if request.method == "POST":
        print(request)
        username = request.POST['username']
        password1 = request.POST['password1']

        user = authenticate(username=username, password=password1)
        if user is not None:
            login(request, user)
            name = user.username
            messages.success(request, "Successfully logged in")

            return redirect('/home/', {'name': name})
        else:
            messages.error(request, "Invalid Username or password")
            return redirect('/home/')

    return render(request, "shop/login.html")


def handlelogout(request):
    # if request.method == 'POST':
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/home')


def Register(request):
    if request.method == "POST":

        # print(request)
        username1 = request.POST['username1']
        email1 = request.POST['email1']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        print(username1, email1, password1, password2)
        # check for error input
        if password1 != password2:
            messages.error(request, "Password did not match")
            return render(request, "home")
        #      create user
        myuser = User.objects.create_user(username1, email1, password1)
        # myuser.password2 = password2
        # myuser.email = email1
        #
        myuser.save()
        messages.success(request, "Your account has been created successfully")
        return redirect('/home/')

    return render(request, "shop/signup.html")
    # else:
    #    return HttpResponse('404 -error')


# return render(request, "shop/login.html")


def search(request):
    query = request.GET.get('query')
    products = Product.objects.all()
    # catviews = Product.objects.all()
    prodtemp = Product.objects.filter(products)
    prod = [item for item in products if searchMatch(query, item)]
    print(products)
    n = len(products)
    nslides = n // 4 + ceil((n / 4) - (n // 4))
    catprods = Product.objects.values('category', 'id')
    subcategory = Product.category
    # productlist = Product.objects.filter(subcategory=subcategory).count()

    params = {'no_of_slides': nslides, 'range': range(nslides), 'product': products, 'catview': catviews,
              'count': productlist}

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


def contact(request):
    if request.method == "POST":
        print(request)
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        print(name, email, phone, subject, message)
        con = Contact(name=name, email=email, phone=phone, subject=subject, message=message)
        con.save()
        # success = '`<div class="alert alert-warning alert-dismissible fade succes" role="alert">  <strong>Hey there!</strong> We have received your message thank you.  <button type="button" class="close" data-dismiss="alert" aria-label="Close">    <span aria-hidden="true">&times;</span>  </button>`'

        return redirect('/home/contact')

    return render(request, "shop/contact.html")


def tracker(request):
    if request.method == "POST":
        orderid = request.POST.get('orderid', '')
        email = request.POST.get('email', '')
        # return HttpResponse(f"{orderid} and {email}")
        try:
            order = Order.objects.filter(order_id=orderid, email=email)
            if len(order) > 0:
                update = Orderupdate.objects.filter(order_id=orderid)
                updates = []
                for item in update:
                    updates.append(
                        {'text': item.update_description, 'time': item.timestamp.strftime("%d-%m-%Y  %H:%M:%S")})
                    response = json.dumps({"status": "success", "updates": updates, "itemsJson": order[0].items_json},
                                          default=str)

                return HttpResponse(response)
            else:
                return HttpResponse('{"status":"noitem"}')
        except Exception as e:
            return HttpResponse('{"status":"error"}')

        return redirect('/home/tracker')

    return render(request, "shop/tracker.html")


@csrf_exempt
def checkout(request):
    if request.method == "POST":
        print(request)
        items_json = request.POST.get('itemsJson', '')
        amount = request.POST.get('amount', '')
        firstname = request.POST.get('firstname', '')
        lastname = request.POST.get('lastname', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        country = request.POST.get('country', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip = request.POST.get('zip', '')
        print(items_json, firstname, lastname, email, phone, address, country, city, state, zip)
        order = Order(items_json=items_json, firstname=firstname, lastname=lastname, email=email, phone=phone,
                      address=address,
                      country=country, city=city, state=state, zip=zip, amount=amount)
        order.save()
        update = Orderupdate(order_id=order.order_id, update_description="Your Order has been placed successfully")
        update.save();
        thank = True
        id = order.order_id

        return render(request, 'shop/checkout.html', {'thank': thank, 'id': id})

        return redirect('/home/checkout')

    return render(request, "shop/checkout.html")


@csrf_exempt
def handlerequest(request):
    return render(request, 'shop/paymentstatus.html')


def thanks(request):
    return render(request, "shop/thanks.html")


def cart(request):
    return render(request, "shop/cart.html")


@csrf_exempt
def stripe_webhook(request):
    print('WEBHOOK!')
    # You can find your endpoint's secret in your webhook settings
    endpoint_secret = 'whsec_f9d1ac74ec539c726403a76acd82024a7f61575df70ecec425b77786ffdc80db'
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        print(session)
        line_items = stripe.checkout.Session.list_line_items(session['id'], limit=1)
        print(line_items)

    return HttpResponse(status=200)
