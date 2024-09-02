from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from . models import Product

from product.models import Product


class ProductDetailView(View):
    def get(self, request, id):
        product = get_object_or_404(Product, id=id)
        return render(request, "product/product_detail.html", {"product": product})

