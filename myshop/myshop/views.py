from django.http import HttpResponse

from django.shortcuts import render


def index(request):
    return render(request, 'Easy_buy/index.html')


def about(request):
    return HttpResponse("THis is about")


def search(request):
    return HttpResponse("THis is search bar")


def contact(request):
    return HttpResponse("THis is contact")


def tracker(request):
    return HttpResponse("THis is trackr")


def checkout(request):
    return HttpResponse("THis is checkout")


def productview(request):
    return HttpResponse('this is product view')
