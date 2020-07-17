from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("search/", views.search, name="Search"),
    path("products/<int:myid>", views.productview, name="Productview"),
    path("checkout/", views.checkout, name="Checkout"),
    path("handlerequest/",views.handlerequest,name="HandleRequest"),
    path("signIn/",views.signIn,name="signIn"),
    path("register/",views.registerPage,name="register"),
    path("login/",views.logIn,name="login"),
    path("logout/",views.logoutUser,name="logout"),
]

