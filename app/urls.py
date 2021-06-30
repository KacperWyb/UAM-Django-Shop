from django.urls import path
from .views import *


app_name = "ecomapp"
urlpatterns = [

    path("", HomeView.as_view(), name="home"),
    path("o-nas/", AboutView.as_view(), name="about"),
    path("kontakt/", ContactView.as_view(), name="contact"),
    path("kategorie/", AllProductsView.as_view(), name="allproducts"),
    path("produkt/<slug:slug>/", ProductDetailView.as_view(), name="productdetail"),

    path("dodaj-do-koszyka-<int:pro_id>/", AddToCartView.as_view(), name="addtocart"),
    path("moj-koszyk/", MyCartView.as_view(), name="mycart"),
    path("koszyk/<int:cp_id>/", ManageCartView.as_view(), name="managecart"),
    path("pusty-koszyk/", EmptyCartView.as_view(), name="emptycart"),

    path("zamowienie/", CheckoutView.as_view(), name="checkout"),

    path("rejestracja/",
         CustomerRegistrationView.as_view(), name="customerregistration"),

    path("wyloguj/", CustomerLogoutView.as_view(), name="customerlogout"),
    path("logowanie/", CustomerLoginView.as_view(), name="customerlogin"),

    path("profil/", CustomerProfileView.as_view(), name="customerprofile"),
    path("profil/zamowienie-<int:pk>/", CustomerOrderDetailView.as_view(),
         name="customerorderdetail"),

    path("szukaj/", SearchView.as_view(), name="search"),

    path("przypomnij-haslo/", PasswordForgotView.as_view(), name="passworforgot"),
    path("zresetuj-haslo/<email>/<token>/",
         PasswordResetView.as_view(), name="passwordreset"),
]
