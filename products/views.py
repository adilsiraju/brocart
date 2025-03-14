from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

# Products list page
def list_products(request):
    return render(request, 'products.html')

# Product detail page
def product_detail(request):
    return render(request, 'product_detail.html')