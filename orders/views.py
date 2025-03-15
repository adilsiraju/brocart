from django.shortcuts import render

# Create your views here.

def show_cart(request):
    return render(request, 'pages/cart.html')