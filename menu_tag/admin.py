from django.contrib import admin
from .models import Menu

# Register your models here.
# admin.site.register(Menu)


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ("pk","cat_name", "parent", "slug")
    list_filter = ("parent",)
    search_fields = ("cat_name", "slug")
    prepopulated_fields = {"slug": ["cat_name"]}
    list_editable = ["parent"]