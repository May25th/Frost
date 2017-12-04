# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone


class Book(models.Model):
    t_id = models.CharField(max_length=32, unique=True),
    name = models.CharField(max_length=64)
    tip = models.CharField(max_length=64, null=True)
    # timestamp = models.DateTimeField(default=timezone.now)

