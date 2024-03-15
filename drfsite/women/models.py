from django.db import models
from .validate_age import validate_age


class Women(models.Model):
    surname = models.CharField(max_length=255, null=False)
    name = models.CharField(max_length=255, null=False)
    age = models.IntegerField(null=False, validators=[validate_age])
    content = models.TextField(blank=True)
    # photo = models.FileField(upload_to="media/%y/%m/%d")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.surname} {self.name}"


class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.title
