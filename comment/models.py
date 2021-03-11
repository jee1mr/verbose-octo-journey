from django.db import models
from page.models import Page
from django.contrib.auth.models import User
from django.contrib import admin


class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    parent = models.ForeignKey("Comment", on_delete=models.CASCADE, null=True, blank=True, related_name="replies")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at', 'pk']

    def __str__(self):
        return self.text


admin.site.register(Comment)
