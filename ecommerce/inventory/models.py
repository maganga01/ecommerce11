from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField


class Category(MPTTModel):
    """Inventory Category table implimented with MPTT."""

    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        unique=True,
        verbose_name=_('Category Name'),
        help_text=_("format: required, max-100")
    )
    slug = models.SlugField(
        max_length=150,
        null=False,
        blank=False,
        unique=True,
        verbose_name=_('Category safe URL'),
        help_text=_("format: required, letters, numbers, hyphens, underscores")
    )
    is_active = models.BooleanField(
        default=False,
    )
    parent = TreeForeignKey(
        'self',
        on_delete=models.PROTECT,
        related_name='children',
        null=True,
        blank=True,
        unique=False,
        verbose_name=_('Parent of Category'),
        help_text=_("format: not required")
    )

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = _('Product Category')
        verbose_name_plural = _('Product Categories')

    def __str__(self):
        return self.name

class Product(models.Model):
    """Inventory Product table implimented with MPTT."""
    name = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        unique=True,
        verbose_name=_('Product Name'),
        help_text=_("format: required, max-100")
    )
    web_id = models.CharField(
        max_length=50,
        unique=True,
        null=False,
        blank=False,
        verbose_name=_('Product Web ID'),
        help_text=_("format: required, max-50, unique")
    )
    slug = models.SlugField(
        max_length=150,
        null=False,
        blank=False,
        unique=True,
        verbose_name=_('Product safe URL'),
        help_text=_("format: required, letters, numbers, hyphens, underscores")
    )
    description = models.TextField(
        max_length=1000,
        null=False,
        blank=False,
        verbose_name=_('Product Description'),
        help_text=_("format: required, max-1000")
    )

    is_active = models.BooleanField(
        default=False,
        unique=False,
        blank=False,
        verbose_name=_('Product visibility'),
        help_text=_("format: required, boolean, true=product is visible, false=product is hidden")
    )
    category = TreeManyToManyField(
        Category,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Created at'),
        help_text=_("format: required")
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Updated at'),
        help_text=_("format: required")
    )

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return self.name


class ProductType(models.Model):
    """Product type table"""
    name = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        unique=True,
        verbose_name=_('Product Type Name'),
        help_text=_("format: required, max-255")
    )

    def __str__(self):
        return self.name

class Brand(models.Model):
    """
    Product brand table
    """

    name = models.CharField(
        max_length=255,
        unique=True,
        null=False,
        blank=False,
        verbose_name=_("brand name"),
        help_text=_("format: required, unique, max-255"),
    )


class ProductInventory(models.Model):
    """
    Product inventory table
    """

    sku = models.CharField(
        max_length=20,
        unique=True,
        null=False,
        blank=False,
        verbose_name=_("stock keeping unit"),
        help_text=_("format: required, unique, max-20"),
    )
    upc = models.CharField(
        max_length=12,
        unique=True,
        null=False,
        blank=False,
        verbose_name=_("universal product code"),
        help_text=_("format: required, unique, max-12"),
    )
    product_type = models.ForeignKey(
        ProductType, related_name="product_type", on_delete=models.PROTECT
    )
    product = models.ForeignKey(
        Product, related_name="product", on_delete=models.PROTECT
    )
    brand = models.ForeignKey(
        Brand, related_name="brand", on_delete=models.PROTECT
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_("product visibility"),
        help_text=_("format: true=product visible"),
    )
    retail_price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("recommended retail price"),
        help_text=_("format: maximum price 999.99"),
        error_messages={
            "name": {
                "max_length": _("the price must be between 0 and 999.99."),
            },
        },
    )
    store_price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("regular store price"),
        help_text=_("format: maximum price 999.99"),
        error_messages={
            "name": {
                "max_length": _("the price must be between 0 and 999.99."),
            },
        },
    )
    sale_price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("sale price"),
        help_text=_("format: maximum price 999.99"),
        error_messages={
            "name": {
                "max_length": _("the price must be between 0 and 999.99."),
            },
        },
    )
    is_on_sale =  models.BooleanField(
        default=False,
    )
    is_digital = models.BooleanField(
        default=False,
    )
    weight = models.FloatField(
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("product weight"),
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
       
    )

    def __str__(self):
        return self.product.name


class ProductAttribute(models.Model):
    """Product attribute table"""

    name = models.CharField(
        max_length=255,
        unique=True,
        null=False,
        blank=False,
        verbose_name=_("product attribute name"),
        help_text=_("format: required, unique, max-255"),
    )
    description = models.TextField(
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("product attribute description"),
        help_text=_("format: required"),
    )

    def __str__(self):
        return self.name

class Media(models.Model):
     """media attribute table"""
     product_inventory = models.ForeignKey(
        ProductInventory,
        on_delete=models.PROTECT,
        related_name-'media',
    )
    img_url = models.ImageField()
    alt_text = models.CharField(
        max_length=255,
    )
    is_feature = models.BooleanField(
        default=False,
    )
    created = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )
    updated = models.DateTimeField(
        auto_now=True,
    )
    
    
class Stock(models.Model):
    product_inventory = models.OneToOneField(
        ProductInventory,
        related_name="product_inventory",
        on_delete=models.PROTECT,
    )
    last_checked = models.DateTimeField(
        null=True,
        blank=True,
    )
    units = models.IntegerField(
        default=0,
    )
    units_sold = models.IntegerField(
        default=0,
    )
    
class ProductAttributeValues(models.Model):
    attributevalues = models.ForeignKey(
        "ProductAttributeValue",
        related_name="attributevalues",
        on_delete=models.PROTECT,
    )
    productinventory = models.ForeignKey(
        ProductInventory,
        related_name"ProductAttributeValues"
        on_delete=models.PROTECT,
    )
    class Meta:
        unique_together = {("attributevalues", "productinventory"),}
        
clas ProductTypeAttribute(models.Model):
    product_attribute = models.ForeignKey(
        ProductAttribute,
        related_name="productattribute",
        on_delete=models.PROTECT,
    )
    product_type = models.ForeignKey(
        ProductType,
        related_name="producttype",
        on_delete=models.PROTECT,
    )
    
    class Meta:
        unique_together = {("product_attribute", "product_type"),}