from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse
from django.contrib import messages
from django.db.models import Q

from .models import Topping, Pizza, Sub, Pasta, Salad, Platter, OrderItem, OnlineOrder
from .forms import SignUpForm

import json

# Create your views here.
def index(request):
    context = {
        'pizzas': Pizza.objects.all(),
        'toppings': Topping.objects.all(),
        'subs': Sub.objects.all(),
        'pastas': Pasta.objects.all(),
        'salads': Salad.objects.all(),
        'platters': Platter.objects.all()
    }
    return render(request, 'orders/index.html', context)

def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(homepage)
        else:
            print("invalid form")

    form = SignUpForm
    return render(request, 'orders/register.html', context={"form": form})

def homepage(request):
    context = {
        'pizzas': Pizza.objects.all(),
        'toppings': Topping.objects.all(),
        'subs': Sub.objects.all(),
        'pastas': Pasta.objects.all(),
        'salads': Salad.objects.all(),
        'platters': Platter.objects.all()
    }
    return render(request, 'orders/homepage.html', context)

def logout_request(request):
    logout(request)
    return redirect(index)

def login_request(request):
    # If login form is posted log user in
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(homepage)
            else:
                messages.info(request, f"Login failed")
    
    # Else render index page            
    form = AuthenticationForm
    return render(request, 'orders/login.html', {"form": form})

def order_request(request):
    context = {
        'pizzas': Pizza.objects.all(),
        'toppings': Topping.objects.all(),
        'subs': Sub.objects.all(),
        'pastas': Pasta.objects.all(),
        'salads': Salad.objects.all(),
        'platters': Platter.objects.all()
    }
         
    return render(request, 'orders/order.html', context=context)

def add_request(request):
    username = request.user.username
    # First check wether user already has an unplaced order
    try:
        current_order = OnlineOrder.objects.get(customer=username, status="unplaced")        
    except OnlineOrder.DoesNotExist:
        current_order = OnlineOrder(customer=username)
        current_order.save()
    print(current_order)
    if request.method == "GET":
        print("GET request detected")
        meal = request.GET["meal"]
        # Check what meal the customer ordered and add the respective item to the online order
        # Add pizza
        if meal == "pizza":
            pizza_type = request.GET["pizza_type"]
            pizza_option = request.GET["pizza_option"]
            size = request.GET["size"]
            price = float(request.GET["price"])
            tops = json.loads(request.GET["toppings"])
            toppings = []
            for top in tops:
                #print(top)
                t = Topping.objects.get(name=top)
                #print(t)
                toppings.append(t)
            #print(toppings)
            new_item = OrderItem(menuItem=meal, meal=meal, pizza_type=pizza_type, size=size, price=price)
            new_item.save()
            for top in toppings:
                new_item.options.add(top)
            new_item.save()
            # Add new_item to online order
            current_order.items.add(new_item)
            current_order.total_price += new_item.price
            current_order.save()
            print(f"Item added")
            
            # Print the log and send response back to the client
            print(f"Following item created: {new_item.meal}, {new_item.pizza_type}, {new_item.size}, {new_item.price}")
            #print(f"Received: {meal}, {pizza_type}, {pizza_option} toppings, {size}, ${price}, {tops}")
            return HttpResponse(f"Added to order: {meal}, {pizza_type}, {pizza_option} toppings, {size}, ${price}, toppings: {tops}")
        # Add sub to order
        elif meal == "sub":
            sub_name = request.GET["sub"]
            size = request.GET["size"]
            price = float(request.GET["price"])
            new_item = OrderItem(menuItem=meal, meal=sub_name, size=size, price=price)
            new_item.save()
            # Add new_item to online order
            current_order.items.add(new_item)
            current_order.total_price += new_item.price
            current_order.save()
            print(f"Item added")
            print(f"Following item created: {new_item.menuItem}, {new_item.meal}, {new_item.size}, {new_item.price}")
            return HttpResponse(f"Added to order: {new_item.menuItem}, {new_item.meal}, {new_item.size}, ${new_item.price}")
        # Add past
        elif meal == "pasta":
            pasta = request.GET["pasta"]
            price = float(request.GET["price"])
            new_item = OrderItem(menuItem=meal, meal=pasta, size="pasta size", price=price)
            new_item.save()
            # Add new_item to online order
            current_order.items.add(new_item)
            current_order.total_price += new_item.price
            current_order.save()
            print(f"Item added")
            print(f"Following item created: {new_item.menuItem}, {new_item.meal}, {new_item.size}, {new_item.price}")
            return HttpResponse(f"Added to order: {new_item.menuItem}, {new_item.meal}, {new_item.size}, ${new_item.price}")
        # Add salad
        elif meal == "salad":
            salad = request.GET["salad"]
            price = float(request.GET["price"])
            new_item = OrderItem(menuItem=meal, meal=salad, size="salad size", price=price)
            new_item.save()
            # Add new_item to online order
            current_order.items.add(new_item)
            current_order.total_price += new_item.price
            current_order.save()
            print(f"Item added")
            print(f"Following item created: {new_item.menuItem}, {new_item.meal}, {new_item.size}, {new_item.price}")
            return HttpResponse(f"Added to order: {new_item.menuItem}, {new_item.meal}, {new_item.size}, ${new_item.price}")
        # Add platter
        elif meal == "platter":
            platter = request.GET["platter"]
            size = request.GET["size"]
            price = float(request.GET["price"])
            new_item = OrderItem(menuItem=meal, meal=platter, size=size, price=price)
            new_item.save()
            # Add new_item to online order
            current_order.items.add(new_item)
            current_order.total_price += new_item.price
            current_order.save()
            print(f"Item added")
            print(f"Following item created: {new_item.menuItem}, {new_item.meal}, {new_item.size}, {new_item.price}")
            return HttpResponse(f"Added to order: {new_item.menuItem}, {new_item.meal}, {new_item.size}, ${new_item.price}")


def shopping_cart(request):
    # Check wether user already has an unplaced order
    try:
        my_order = OnlineOrder.objects.get(customer=request.user.username, status="unplaced")
        context = {"items": my_order.items.all(), "price": my_order.total_price}       
    except OnlineOrder.DoesNotExist:
        context = {"items": None}

    # On POST cancel or place the order
    if request.method == "POST":
        if 'place' in request.POST:
            # Place the order
            print("Place the order")
            my_order.status = "placed"
            my_order.save()
            return redirect(tracker)
        elif 'cancel' in request.POST:
            # Cancel the order
            my_order.delete()
            print("Cancel the order")
            return redirect(homepage)
    return render(request, 'orders/shoppingcart.html', context=context)

def tracker(request):
    try:
        my_order = OnlineOrder.objects.get(Q(customer=request.user.username) & (Q(status = "placed") | Q(status = "preparing") | Q(status="cooking") | Q(status="finished")))
        context = {"items": my_order.items.all(), "price": my_order.total_price, "status": my_order.status, "customer": my_order.customer}       
    except OnlineOrder.DoesNotExist:
        context = {"items": None}
    return render(request, 'orders/tracker.html', context=context)

def staffpage(request):
    if request.user.is_staff:
        try:
            placed_orders = OnlineOrder.objects.filter(status ="placed")
        except OnlineOrder.DoesNotExist:
            placed_orders = None
        
        try:
            preparing_orders = OnlineOrder.objects.filter(status ="preparing")
        except OnlineOrder.DoesNotExist:
            preparing_orders = None

        try:
            cooking_orders = OnlineOrder.objects.filter(status ="cooking")
        except OnlineOrder.DoesNotExist:
            cooking_orders = None
        
        try:
            finished_orders = OnlineOrder.objects.filter(status ="finished")
        except OnlineOrder.DoesNotExist:
            finished_orders = None

        try:
            delivered_orders = OnlineOrder.objects.filter(status ="delivered")
        except OnlineOrder.DoesNotExist:
            delivered_orders = None
        
        context = {
            "staff_authenticated": True,
            'placed_orders': placed_orders,
            'preparing_orders': preparing_orders,
            'cooking_orders': cooking_orders,
            'finished_orders': finished_orders,
            'delivered_orders': delivered_orders
        }        
        return render(request, 'orders/staffpage.html', context=context)
    else:
        return render(request, 'orders/staffpage.html', context={"staff_authenticated": False})

def order_process(request, order_id):
    try:
        order = OnlineOrder.objects.get(pk=order_id)
        context = {"items": order.items.all(), "price": order.total_price, "status": order.status}       
    except OnlineOrder.DoesNotExist:
        context = {"items": None}
    if request.method == "POST":
        new_status = request.POST.getlist("new_status")[0]
        order.status = new_status
        order.save()
        return redirect(staffpage)
    return render(request, 'orders/orderprocess.html', context=context)
