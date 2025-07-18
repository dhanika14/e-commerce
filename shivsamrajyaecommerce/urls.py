"""
URL configuration for shivsamrajyaecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from shivsamrajyaecommerce import settings,views
from django.conf.urls.static import static # type: ignore
from .views import registration


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('contactus/',views.contactus),
    path('login/',views.login),
    path('logout/',views.logout),
    path('registration/',views.registration),
    path('about/',views.about),
    path('general/',views.general),
    path('cosmetic/',views.cosmetic),
    path('spices/',views.Spices),
    path('general/',views.general),
    path('fooditems/',views.fooditems),
    path('shop/',views.shop),
    path('grocery/',views.grocery),
    path('stationary/',views.stationary),
    path('checkout/',views.checkout),

   

    path('bill/',views.bill),
    # path('showitem/',views.showitem),
    path('thankyou/',views.thankyou),


    # path('cart/',views.cart),

    path('submit/',views.submit),
    path('slider/',views.slider),
    path("contfrom/",views.sub),
    path('Grocery/',views.grocery),
    path('General/',views.general),
    path('Food Items/',views.fooditems),
    path('Spices/',views.Spices),
    path('Stationary/',views.stationary),
    path('Cosmetic/',views.cosmetic),

    path('view_cart/',views.view_cart),

   
    path('cart_submit/',views.cart_submit),
    path('wishlist_add/',views.wishlist_add),
    

    path('wishlist/',views.wishlist),
    path("wishlistdelete/<id>/",views.wishlistdelete),
    path("cart_delete<id>/",views.cartdelete),
   
    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 
