from django.shortcuts import render
from . models import Product
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    featured_products = Product.objects.order_by('-priority')[:4]
    latest_products = Product.objects.order_by('-id')[:4]

    context = {
        'featured_products' : featured_products,
        'latest_products' : latest_products
    }

    return render(request, 'pages/index.html', context)

# Products list page
def list_products(request):
    """
    Handle product listing with pagination functionality.
    This view function retrieves all products from the database and implements
    pagination to display them in chunks of 2 items per page. The current page
    number can be specified through the 'page' GET parameter.
    Args:
        request: HttpRequest object containing metadata about the request.
    Returns:
        HttpResponse: Rendered template 'pages/products.html' with paginated products
                     in the context.
    Context:
        products: Page object containing a subset of Product instances for the
                 current page.
    """
    # Default page number
    page = 1
    # Get page number from GET request
    # If page number is not specified, default to 1
    if request.GET:
        page = request.GET.get('page', 1)

    # Get all products
    product_list = Product.objects.order_by('-priority')

    # Create paginator object with product_list and 2 items per page
    product_paginator = Paginator(product_list, 4)

    # Get page of the paginated results
    product_list = product_paginator.get_page(page)

    # Context for template page
    context = {
        'products' : product_list
    }

    return render(request, 'pages/products.html', context)

# Product detail page
def product_detail(request, pk):

    product = Product.objects.get(pk=pk)
    context = {
        'product' : product
    }

    return render(request, 'pages/product_detail.html', context)