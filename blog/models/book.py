# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone


class Book(models.Model):
    author = models.IntegerField(),
    name = models.CharField(max_length=64)
    tip = models.CharField(max_length=64)
    create_at = models.DateTimeField(auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True)

