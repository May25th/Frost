# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone


class Book(models.Model):
    t_id = models.CharField(max_length=32, unique=True),
    name = models.CharField(max_length=64)
    tip = models.CharField(max_length=64, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True)

