from django.db import models
from django.contrib.auth.models import User

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="admins")
    mobile = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imię_i_nazwisko = models.CharField(max_length=200)
    adres = models.CharField(max_length=200, null=True, blank=True)
    joined_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.imię_i_nazwisko


class Categorie(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products")
    marked_price = models.PositiveIntegerField()
    selling_price = models.PositiveIntegerField(default=0)
    description = models.TextField()
    warranty = models.CharField(max_length=300)
    return_policy = models.CharField(max_length=300)
    view_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products/images/")

    def __str__(self):
        return self.product.title


class Cart(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True, blank=True)
    total = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Cart: " + str(self.id)


class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rate = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    subtotal = models.PositiveIntegerField()

    def __str__(self):
        return "Cart: " + str(self.cart.id) + " CartProduct: " + str(self.id)


ORDER_STATUS = (
    ("Otrzymano zamówienie", "Otrzymano zamówienie"),
    ("Przetwarzanie zamówienia", "Przetwarzanie zamówienia"),
    ("W drodze", "W drodze"),
    ("Zamówienie zrealizowane", "Zamówienie zrealizowane"),
    ("Zamówienie anulowane", "Zamówienie anulowane"),
)

METHOD = (
    ("Za pobraniem", "Za pobraniem"),
    ("PayPal", "PayPal"),
    ("Przelewy24", "Przelewy24"),
)


class Order(models.Model):
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    zamówiony_przez = models.CharField(max_length=200) #, default=str(Customer))
    adres_wysyłki = models.CharField(max_length=200)
    telefon = models.CharField(max_length=10)
    email = models.EmailField(null=True, blank=True)
    subtotal = models.PositiveIntegerField()
    discount = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
    order_status = models.CharField(max_length=50, choices=ORDER_STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    metoda_płatności = models.CharField(
        max_length=20, choices=METHOD, default="Za pobraniem")
    payment_completed = models.BooleanField(
        default=False, null=True, blank=True)

    def __str__(self):
        return "Order: " + str(self.id)
