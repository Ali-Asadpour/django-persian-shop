from django.contrib import admin
from product import models


class ShortInfoInline(admin.StackedInline):
    model = models.ShortInfo
    extra = 1


class ImageInline(admin.StackedInline):
    model = models.Image
    extra = 1


class GoodBadInline(admin.StackedInline):
    model = models.GoodOrBadPoint
    extra = 1


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
