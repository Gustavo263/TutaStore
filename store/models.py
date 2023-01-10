from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    """
    Category Table implimented with MPTT.
    """

    name = models.CharField(
        verbose_name=_("Nome da Categoria"),
        help_text=_("Obrigatório"),
        max_length=255,
        unique=True,
    )
    slug = models.SlugField(verbose_name=_("URL da categoria"), max_length=255, unique=True)
    parent = TreeForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="children")
    is_active = models.BooleanField(verbose_name=_("Ativar Produto"), default=True)

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def get_absolute_url(self):
        return reverse("store:category_list", args=[self.slug])

    def __str__(self):
        return self.name


class ProductType(models.Model):
    """
    ProductType Table will provide a list of the different types
    of products that are for sale.
    """

    name = models.CharField(verbose_name=_("Tipo do Produto"), help_text=_("Obrigatório"), max_length=255, unique=True)
    is_active = models.BooleanField(verbose_name=_("Ativar Produto"), default=True)

    class Meta:
        verbose_name = _("Product Type")
        verbose_name_plural = _("Product Types")

    def __str__(self):
        return self.name


class ProductSpecification(models.Model):
    """
    The Product Specification Table contains product
    specifiction or features for the product types.
    """

    product_type = models.ForeignKey(ProductType, on_delete=models.RESTRICT)
    name = models.CharField(verbose_name=_("Nome"), help_text=_("Obrigatório"), max_length=255)

    class Meta:
        verbose_name = _("Product Specification")
        verbose_name_plural = _("Product Specifications")

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    The Product table contining all product items.
    """

    product_type = models.ForeignKey(ProductType, verbose_name=_("Tipo do Produto"), on_delete=models.RESTRICT)
    category = models.ForeignKey(Category, verbose_name=_("Categoria do Produto"), on_delete=models.RESTRICT)
    title = models.CharField(
        verbose_name=_("Título "),
        help_text=_("Obrigatório"),
        max_length=255,
    )
    description = models.TextField(verbose_name=_("Descrição"), help_text=_("Não Obrigatório"), blank=True)
    slug = models.SlugField(max_length=255)
    regular_price = models.DecimalField(
        verbose_name=_("Preço regular"),
        help_text=_("Máximo 999.99"),
        error_messages={
            "name": {
                "max_length": _("O preço deve estar entre 0 e 999.99."),
            },
        },
        max_digits=5,
        decimal_places=2,
    )
    discount_price = models.DecimalField(
        verbose_name=_("Preço com desconto"),
        help_text=_("Máximo 999.99"),
        error_messages={
            "name": {
                "max_length": _("O preço deve estar entre 0 e 999.99."),
            },
        },
        max_digits=5,
        decimal_places=2,
    )
    is_active = models.BooleanField(
        verbose_name=_("Visibilidade do produto"),
        help_text=_("Alterar a visibilidade do produto"),
        default=True,
    )
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)
    users_wishlist = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="user_wishlist", blank=True)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def get_absolute_url(self):
        return reverse("store:product_detail", args=[self.slug])

    def __str__(self):
        return self.title


class ProductSpecificationValue(models.Model):
    """
    The Product Specification Value table holds each of the
    products individual specification or bespoke features.
    """

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    specification = models.ForeignKey(ProductSpecification, on_delete=models.RESTRICT)
    value = models.CharField(
        verbose_name=_("Valor"),
        help_text=_("Valor da especificação do produto (máximo de 255 palavras)"),
        max_length=255,
    )

    class Meta:
        verbose_name = _("Product Specification Value")
        verbose_name_plural = _("Product Specification Values")

    def __str__(self):
        return self.value


class ProductImage(models.Model):
    """
    The Product Image table.
    """

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_image")
    image = models.ImageField(
        verbose_name=_("Imagem"),
        help_text=_("Carregue uma imagem do produto"),
        upload_to="images/",
        default="images/default.png",
    )
    alt_text = models.CharField(
        verbose_name=_("Texto alternativo"),
        help_text=_("Por favor, adicione texto alternativo"),
        max_length=255,
        null=True,
        blank=True,
    )
    is_feature = models.BooleanField(verbose_name=_("Principal"), default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Product Image")
        verbose_name_plural = _("Product Images")
