# -*- coding: utf-8 -*-
from django.db import models


class Book(models.Model):
    t_id = models.CharField(max_length=32, unique=True),
    name = models.CharField(max_length=64)
    timestamp = models.DateTimeField()

