from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.
def index_view(request):
    products = Product.objects.filter(is_active=True)

    return render(request, 'main/index.html', {"products": products})

def product_detail_view(request, product_id):
    # product = Product.objects.get(id=product_id)
    product = get_object_or_404(Product, id=product_id)
    similar_products = Product.objects.filter(category=product.category).execute(id=product.id)

    return render (
        request=request,
        template_name='main/product_detail.html',
        context={"product": product, "similar_products": similar_products})