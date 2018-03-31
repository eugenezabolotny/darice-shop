# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import ArrayField


class Product(models.Model):

    item = models.PositiveIntegerField(null=False)
    image = models.CharField(max_length=500)
    upc = models.PositiveIntegerField(null=False)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    case_pack = models.PositiveIntegerField(null=False)
    inner_pack = models.PositiveIntegerField(null=False)
    in_stock = models.BooleanField()
    color = models.CharField(max_length=60)
    shape = models.CharField(max_length=60)
    images = ArrayField(models.CharField(max_length=500))
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.item
