from django.db import models
from django.urls import reverse
# Create your models here.
class Menu(models.Model):
    cat_name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.cat_name}" 

    def get_absolute_url(self):
        return reverse("menu_slug", kwargs={"menu_slug": self.slug})