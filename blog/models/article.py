# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone


class Article(models.Model):
    author = models.IntegerField(default=0),
    name = models.CharField(max_length=64, default='')
    text = models.TextField(max_length=16384, null=False)
    create_at = models.DateTimeField(auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True)

