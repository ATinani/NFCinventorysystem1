from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Product,Order
from .forms import ProductForm,OrderForm
from django.contrib.auth.models import User
from django.contrib import messages
from datetime import date
from django.db.models import Sum
from django.shortcuts import get_object_or_404



# Create your views here.

from django.contrib.auth import authenticate, login

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard-index')
        else:
            messages.error(request, 'Invalid credentials')

    return render(request, 'auth/login.html')


@login_required(login_url='user-login')
def index(request):
    orders = Order.objects.all()
    products = Product.objects.all()
    orders_count = Order.objects.all().count()
    product_count = Product.objects.all().count()
    workers_count = User.objects.all().count()


    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            #form.save()
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('dashboard-index')
    else:
        form = OrderForm()

    context={
        'orders': orders,
        'form': form,
        'products': products,
        'workers_count': workers_count,
        'orders_count': orders_count,
        'product_count': product_count,
    }
    return render(request,'dashboard/index.html',context)

@login_required(login_url='user-login')
def staff(request):
    workers = User.objects.all()
    workers_count = workers.count()
    orders_count = Order.objects.all().count()
    product_count = Product.objects.all().count()


    context={
        'workers':workers,
        'workers_count': workers_count,
        'orders_count': orders_count,
        'product_count': product_count,

    }
    return render(request,'dashboard/staff.html',context)

@login_required(login_url='user-login')
def staff_detail(request,pk):
    workers = User.objects.get(id=pk)
    context = {
        'workers':workers,
    }
    return render(request,'dashboard/staff_detail.html',context)

@login_required(login_url='user-login')
def product(request):
    items = Product.objects.all() #using ORM
    workers_count = User.objects.all().count()
    orders_count = Order.objects.all().count()
    product_count = items.count()



    #workers_count = workers.count()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request,f'{product_name} has been added')
            return redirect('dashboard-product')
    else:
        form = ProductForm()
    context = {
        'items': items,
        'form': form,
        'workers_count': workers_count,
        'orders_count': orders_count,
        'product_count': product_count,

    }
    return render(request,'dashboard/product.html',context)

@login_required(login_url='user-login')
def order(request):
    orders = Order.objects.all()
    workers_count = User.objects.all().count()
    orders_count = orders.count()
    product_count = Product.objects.all().count()


    context = {
        'orders': orders,
        'workers_count': workers_count,
        'orders_count': orders_count,
        'product_count': product_count,

    }


    return render(request,'dashboard/order.html',context)


@login_required(login_url='user-login')
def warehouse_stock_view(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'warehouse_stock.html', context)



@login_required(login_url='user-login')
def update_stock_view(request):
    if request.method == 'POST':
        product_id = request.POST.get('product')
        quantity = int(request.POST.get('quantity'))
        
        # Fetch product and update stock
        product = get_object_or_404(Product, id=product_id)
        product.quantity += quantity
        product.save()

        messages.success(request, f"{quantity} added to {product.name}. New stock: {product.quantity}")
    return redirect('warehouse-stock')


@login_required(login_url='user-login')
def used_stock(request):
    if request.method == 'POST':
        product_id = request.POST.get('product')
        quantity_used = int(request.POST.get('quantity'))

        try:
            product = Product.objects.get(id=product_id)
            if product.quantity >= quantity_used:
                product.quantity -= quantity_used  # Subtract the used quantity
                product.save()  # Save the updated product
            else:
                # Handle case where not enough stock is available
                pass

        except Product.DoesNotExist:
            # Handle case where product doesn't exist
            pass

        return redirect('used-stock')  # Redirect to the same page to refresh the stock table

    # If GET request, simply fetch the products
    products = Product.objects.all()
    return render(request, 'used-stock.html', {'products': products})








@login_required(login_url='user-login')
def product_delete(request,pk):
    item = Product.objects.get(id=pk)
    if request.method=='POST':
        item.delete()
        return redirect('dashboard-product')
    return render(request,'dashboard/product_delete.html')


@login_required(login_url='user-login')
def product_update(request,pk):
    item = Product.objects.get(id=pk)
    if request.method=='POST':
        form = ProductForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form = ProductForm(instance=item)
    context = {
        'form': form,

    }
    return render(request,'dashboard/product_update.html',context)