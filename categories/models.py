from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    tagline = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

    @property
    def get_category_count(self):
        return self.objects.all().count()

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Categories"
