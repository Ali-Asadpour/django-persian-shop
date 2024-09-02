from django.contrib import admin
from product import models


class ShortInfoInline(admin.StackedInline):
    model = models.ShortInfo


class ImageInline(admin.StackedInline):
    model = models.Image


class GoodBadInline(admin.StackedInline):
    model = models.GoodOrBadPoint


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("show_image",'name', 'price', 'marketer',)
    fields = ["name","brand","category","color","marketer","price","discount","numbers","description", "sales"]
    inlines = [ImageInline, ShortInfoInline, GoodBadInline]
    list_filter = ['marketer', 'category',"brand"]
    search_fields = ['name']


admin.site.register(models.Brand)
admin.site.register(models.Color)
admin.site.register(models.Category)
