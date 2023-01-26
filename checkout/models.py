from django.db import models
from django.utils.translation import gettext_lazy as _


class DeliveryOptions(models.Model):
    DELIVERY_CHOICES = [
        ("RL", "Retirar na loja"),
        ("EC", "Entrega em casa"),
        ("ED", "Entrega digital"),
    ]

    delivery_name = models.CharField(
        verbose_name=_("Tipo de entrega"),
        help_text=_("Necessário"),
        max_length=255,
    )
    delivery_price = models.DecimalField(
        verbose_name=_("Preço da entrega"),
        help_text=_("Máximo 999.99"),
        error_messages={
            "name": {
                "max_length": _("O preço deve estar entre 0 e 999.99."),
            },
        },
        max_digits=5,
        decimal_places=2,
    )
    delivery_method = models.CharField(
        choices=DELIVERY_CHOICES,
        verbose_name=_("Método da entrega"),
        help_text=_("Necessário"),
        max_length=255,
    )
    delivery_timeframe = models.CharField(
        verbose_name=_("Prazo de entrega"),
        help_text=_("Necessário"),
        max_length=255,
    )
    delivery_window = models.CharField(
        verbose_name=_("Horário de entrega"),
        help_text=_("Necessário"),
        max_length=255,
    )
    order = models.IntegerField(verbose_name=_("Ordem da lista"), help_text=_("Necessário"), default=0)
    is_active = models.BooleanField(verbose_name=_("Ativar"), default=True)

    class Meta:
        verbose_name = _("Delivery Option")
        verbose_name_plural = _("Delivery Options")

    def __str__(self):
        return self.delivery_name


class PaymentSelections(models.Model):
    """
    Store payment options
    """

    name = models.CharField(
        verbose_name=_("Nome"),
        help_text=_("Necessário"),
        max_length=255,
    )

    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Payment Selection")
        verbose_name_plural = _("Payment Selections")

    def __str__(self):
        return self.name
