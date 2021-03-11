from django.db import models
from django.contrib import admin


class Page(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()

    def __str__(self):
        return self.name


admin.site.register(Page)
