from decimal import Decimal

from django.conf import settings
from django.db import models

from store.models import Product


class Order(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name=("Usuário"), on_delete=models.CASCADE, related_name="order_user"
    )
    full_name = models.CharField(verbose_name=("Nome do Cliente"), max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    address1 = models.CharField(verbose_name=("Endereço 1"), max_length=250)
    address2 = models.CharField(verbose_name=("Endereço 2"), max_length=250)
    city = models.CharField(verbose_name=("Cidade"), max_length=100)
    phone = models.CharField(verbose_name=("Número do telefone"), max_length=100)
    postal_code = models.CharField(verbose_name=("Codigo Postal"), max_length=20)
    country_code = models.CharField(verbose_name=("Código do País"), max_length=4, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    total_paid = models.DecimalField(verbose_name=("Preço pago"), max_digits=5, decimal_places=2)
    order_key = models.CharField(verbose_name=("Chave do pedido"), max_length=200)
    payment_option = models.CharField(verbose_name=("Forma do pagamento"), max_length=200, blank=True)
    billing_status = models.BooleanField(verbose_name=("Status de cobrança"), default=False)

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return str(self.created)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, verbose_name=("Data de compra"), related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, verbose_name=("Produto"), related_name="order_items", on_delete=models.CASCADE
    )
    price = models.DecimalField(verbose_name=("Preço"), max_digits=5, decimal_places=2)
    quantity = models.PositiveIntegerField(verbose_name=("Quantidade"), default=1)

    def __str__(self):
        return str(self.id)
