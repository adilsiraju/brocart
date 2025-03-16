from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from . models import Customer
from django.shortcuts import redirect
from django.contrib import messages

# Create your views here.

def show_account(request):
    context = {}

    # Check if the request is POST and contains 'register' in POST data
    if request.POST and 'register' in request.POST:

        context['register'] = True

        try:
            # Get username from POST data
            username = request.POST.get('username')
            # Get password from POST data
            password = request.POST.get('password')
            # Get email from POST data
            email = request.POST.get('email')
            # Get address from POST data
            address = request.POST.get('address')
            # Get phone number from POST data
            phone = request.POST.get('phone')
            
            # Create a new user 
            user = User.objects.create_user(username, email, password)

            # Create Customer_account for the user
            customer = Customer.objects.create(
                name=username,
                address=address,
                phone=phone,
                email=email,
                user=user
            )

            success_message = 'Account Created Successfully'
            messages.success(request, success_message)
        
        except Exception as e:
            # If there is an error, print the error message
            # and display it to the user
            error_message = 'Duplicate username, or invalid input'
            messages.error(request, error_message)
            print(e)
    
    if request.POST and 'login' in request.POST:

        context['register'] = False

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid Credentials'
            messages.error(request, error_message)

    return render(request, 'pages/account.html', context)

def sign_out(request):
    logout(request)
    return redirect('home')