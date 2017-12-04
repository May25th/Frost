# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone


class Article(models.Model):
    author = models.IntegerField(),
    name = models.CharField(max_length=64)
    text = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True)

