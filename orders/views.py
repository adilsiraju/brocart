from django.shortcuts import render
from . models import Order, OrderedItem
from products.models import Product
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def show_cart(request):
    
    # Get the current user
    user = request.user
    # Get the customer profile of the
    customer = user.customer_profile
    # Get the cart object for the customer
    cart_obj, created = Order.objects.get_or_create(
        owner = customer,
        order_status = Order.CART_STAGE
    )
    
    context = {
        'cart': cart_obj
    }
    
    return render(request, 'pages/cart.html', context)

@login_required(login_url='account')
def show_orders(request):
    
    # Get the current user
    user = request.user
    customer = user.customer_profile
    
    all_orders = Order.objects.filter(owner = customer).exclude(order_status = Order.CART_STAGE)

    context = {
        'orders': all_orders
    }
    
    return render(request, 'pages/orders.html', context)


@login_required(login_url='account')
def add_to_cart(request):
    if request.POST:
        # Get the current user
        user = request.user
        # Get the customer profile of the user
        customer = user.customer_profile

        # Get the product id and quantity from the form
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity'))

        # This code either retrieves an existing Order object or creates a new one:
        # 1. It looks for an Order with the specified owner (customer) and order_status=CART_STAGE
        # 2. If found, returns (existing_order, False)
        # 3. If not found, creates new Order and returns (new_order, True)
        cart_obj,created = Order.objects.get_or_create(
            owner = customer,
            order_status = Order.CART_STAGE
        )

        # Get the product object from the database
        product = Product.objects.get(pk=product_id)

        # This code either retrieves an existing OrderedItem object or creates a new one:
        # 1. It looks for an OrderedItem with the specified product, order, and quantity
        # 2. If found, returns (existing_ordered_item, False)
        # 3. If not found, creates new OrderedItem and returns (new_ordered_item, True  )
        ordered_item, created = OrderedItem.objects.get_or_create(
            product = product,
            order = cart_obj
        )

        # If the OrderedItem already exists, update the quantity
        # Otherwise, create a new OrderedItem
        if created:
            ordered_item.quantity = quantity
            ordered_item.save()
        else:
            ordered_item.quantity += quantity
            ordered_item.save()

    return redirect ('cart')

def remove_item_from_cart(request, pk):
    item = OrderedItem.objects.get(pk = pk)
    if item:
        item.delete()
    return redirect('cart')

def checkout_cart(request):
    if request.POST:

        try:

            # Get the current user
            user = request.user
            customer = user.customer_profile

            # Get the total amount from the form
            # This is the total amount to be paid by the customer
            total = float(request.POST.get('total'))
            
            # Get the cart object for the customer
            order_obj = Order.objects.get(
                owner = customer,
                order_status = Order.CART_STAGE
            )

            # Update the order status to ORDER_CONFIRMED
            # This marks the order as confirmed and ready for processing
            if order_obj:
                order_obj.order_status = Order.ORDER_CONFIRMED
                order_obj.total_amount = total
                order_obj.save()

                status_message = 'Order Confirmed!, Your items will be delivered soon'
                messages.success(request, status_message)

            # If the order is not found, display an error message
            else:
                status_message = 'Order not found'
                messages.error(request, status_message)

        # If an error occurs, display the error message
        except Exception as e:
            status_message = 'Error: ' + str(e)
            messages.error(request, status_message)
            
    return redirect('cart')