from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import Product, Category

from product.models import Product


class ProductDetailView(View):
    def get(self, request, id):
        product = get_object_or_404(Product, id=id)
        return render(request, "product/product_detail.html", {"product": product})






class ProductListView(View):
    def get(self, request):
        products = Product.objects.all()
        categories = Category.objects.all()

        min_price = request.GET.get('min_price')
        max_price = request.GET.get('max_price')
        category_list = request.GET.getlist('category')
        search = request.GET.get('search')

        if len(category_list) > 0:
            products = products.filter(category__name__in=category_list)


        if search:
            products = products.filter(name__contains=search).distinct()


        if min_price and max_price:
            try:
                products = products.filter(price__gt=int(min_price), price__lt=int(max_price))
            except:
                pass
        elif min_price:
            try:
                products = products.filter(price__gt=int(min_price))
            except:
                pass
        elif max_price:
            try:
                products = products.filter(price__lt=int(max_price))
            except:
                pass



        return render(request, "product/product_list.html", {"products": products, "categories": categories, "active_categories":category_list})