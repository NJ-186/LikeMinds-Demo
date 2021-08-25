from django.db import models
from django.db.models.query_utils import Q
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Item(models.Model):
    itemCategory = models.CharField(
        max_length=100,
        help_text=_(
            'item category'
        )
    )
    brand = models.CharField(
        max_length=100,
        help_text=_(
            'brand of the item'
        )
    )
    price = models.IntegerField(
        help_text=_(
            'price for the item'
        )
    )


class Inventory(models.Model):
    item = models.ForeignKey(
        Item,
        on_delete=models.PROTECT
    )
    quantity = models.IntegerField(
        help_text=_(
            'quantity for the item'
        )
    )


class User(models.Model):
    userName = models.CharField(
        max_length=100,
        help_text=_(
            'username'
        )
    )
    walletAmount = models.IntegerField(
        help_text=_(
            'wallet amount'
        )
    )


class Cart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT
    )
    item = models.ForeignKey(
        Item,
        on_delete=models.PROTECT
    )
    quantity = models.IntegerField(
        help_text=_(
            'quantity for the item'
        )
    )
    