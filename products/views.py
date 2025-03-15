from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'pages/index.html')

# Products list page
def list_products(request):
    return render(request, 'pages/products.html')

# Product detail page
def product_detail(request):
    return render(request, 'pages/product_detail.html')