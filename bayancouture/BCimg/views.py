from itertools import product
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from BCimg.models import couture
from django.contrib.auth import authenticate, login , logout
from django.shortcuts import render, redirect
from .forms import AddToCartForm, AddabayaForm, LoginForm , RegistrationForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from BCimg.models import Cart, product, CartItem





# Create your views here.
def Home_list(request):
    # Get the username if the user is authenticated
    username = ""
    if request.user.is_authenticated:
        username = request.user.username

    context = {
        'username': username  # Pass the username to the template
    }
    
    return render(request, 'couture/index.html', context)

def Product_list(request):
    couture_objects = couture.objects.all()
    
    # Get the username if the user is authenticated
    username = ""
    if request.user.is_authenticated:
        username = request.user.username

    context = {
        'couture_objects': couture_objects,
        'username': username  # Pass the username to the template
    }
    
    return render(request, 'couture/product_page.html', context)



def About_list(request):
    # Get the username if the user is authenticated
    username = ""
    if request.user.is_authenticated:
        username = request.user.username

    context = {
        'username': username  # Pass the username to the template
    }
    
    return render(request, 'couture/about_page.html', context)

def search(request):
    query = request.GET.get('q')

    if query:
        products = couture.objects.filter(code__icontains=query)
    else:
        products = couture.objects.all()

    context = {
        'products': products,
        'query': query
    }

    return render(request, 'couture/search_results.html', context)



def register(request):
   if request.method == 'POST':
      form = RegistrationForm(request.POST)
      if form.is_valid():
          form.save()
            
      return redirect('login')
   else:
        form = RegistrationForm()
        return render(request, 'couture/register.html', {'form': form})


def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to the home page after login
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()

    return render(request, 'couture/login.html', {'form': form})


@login_required
def view_cart(request):
    cart_items = CartItem.objects.filter(cart__user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'couture/cart.html', {'cart_items': cart_items, 'total_price': total_price})



def logout_view(request):
    logout(request)
    return redirect('home')



def add_to_cart(request, product_id):
    print(f"add_to_cart view called with product_id={product_id}")

    if request.method == 'POST':
        print("POST request received")

        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return redirect('login')  # Redirect to the login page if the user is not authenticated

        # Get the product based on the provided product ID
        product = get_object_or_404(couture, id=product_id)

        # Get the user's cart or create a new one if it doesn't exist
        cart, created = Cart.objects.get_or_create(user=request.user)

        # Process the form data
        form = AddToCartForm(request.POST)
        if form.is_valid():
            print("Form is valid")

            quantity = form.cleaned_data['quantity']

            # Check if the item is already in the cart
            cart_item = CartItem.objects.filter(cart=cart, product=product).first()

            if cart_item:
                # If the item is already in the cart, update the quantity
                cart_item.quantity += quantity
                cart_item.save()
            else:
                # If the item is not in the cart, create a new cart item
                CartItem.objects.create(cart=cart, product=product, quantity=quantity)

            # Redirect to the cart page
            return redirect('view_cart')  # Use the name of the cart view URL pattern

        else:
            print("Form is not valid")
            print(form.errors)

    return redirect('home')  # Adjust this if you have a different URL for the home page


@login_required
def cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    cart_items = cart.cartitem_set.all()
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    context = {
        'cart_items': cart_items,
        'total_price': total_price
    }
    return render(request, 'couture/cart.html', context)
                                          

def product_detail(request, product_id):
    product = get_object_or_404(couture, id=product_id)
    return render(request, 'couture/product_detail.html', {'product': product})

##@login_required  # Require authentication to access this view
##def add_to_cart(request, product_id):
  ##cart, created = Cart.objects.get_or_create(user=request.user)  
    ##cart.products.add(product)
    ##return redirect('cart.html')  # Redirect to the cart page after adding the product


def cart_view(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')  # Assuming you have a hidden input with the name 'product_id' in your form
        add_to_cart(request, product_id)  # Pass the product_id argument to the add_to_cart function



@login_required(login_url='login')  
def addabaya(request):
    if request.method == 'POST':
        form = AddabayaForm(request.POST, request.FILES)
        if form.is_valid():
            abaya = form.save(commit=False)
            abaya.save()
            return redirect('product')
    else:
        form = AddabayaForm()
    return render(request, 'couture/addabaya.html', {'form': form})