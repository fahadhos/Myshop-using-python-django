"""myshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views
# from .views import redirect_view
from .views import stripe_webhook

urlpatterns = [
                  # path('admin/', admin.site.urls),
                  # path('/redirect/', redirect_view),
                  path('', views.index, name='Home'),
                  path('about/', views.about, name='AboutUs'),
                  path('detail/<int:pid>', views.detail, name='Detail'),
                  path('contact/', views.contact, name='ContactUs'),
                  path('tracker/', views.tracker, name='trackingstatus'),
                  path('search/', views.search, name='Search'),
                  path('login/', views.Login, name='Login'),
                  path('logout/', views.handlelogout, name='Logout'),
                  path('register/', views.Register, name='register'),
                  path('product', views.product, name='ProductView'),
                  # path('product/', views.shop, name='ShopView'),
                  path('cart/', views.cart, name='CartView'),
                  path('checkout/', views.checkout, name='checkout'),
                  path('thanks/', views.thanks, name='thanks'),
                  path('handlerequest/', views.handlerequest, name='handlerequest'),
                  path('stripe_webhook/', views.stripe_webhook, name='stripe_webhook'),

              ]
