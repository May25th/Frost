# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone


class Article(models.Model):
    author = models.IntegerField(default=0),
    name = models.CharField(max_length=64, null=False)
    text = models.TextField(null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True)

