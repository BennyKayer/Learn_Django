from django.shortcuts import render, redirect
from .models import Customer, Product, Order
from .forms import OrderForm

# Create your views here.


def home(req):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status="Delivered").count()
    pending = orders.filter(status="Pending").count()

    context = {
        "orders": orders,
        "customers": customers,
        "total_orders": total_orders,
        "total_customers": total_customers,
        "delivered": delivered,
        "pending": pending,
    }

    return render(req, "accounts/dashboard.html", context)


def products(req):
    products = Product.objects.all()
    return render(req, "accounts/products.html", {"products": products})


def customer(req, pk):
    customer = Customer.objects.get(id=pk)

    orders = customer.order_set.all()
    order_count = orders.count()

    context = {
        "customer": customer,
        "orders": orders,
        "order_count": order_count,
    }
    return render(req, "accounts/customer.html", context)


def createOrder(request):

    form = OrderForm()
    if request.method == "POST":
        # print("Printing POST", request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {"form": form}

    return render(request, "accounts/order_form.html", context)


def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {"form": form}

    return render(request, "accounts/order_form.html", context)


def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    context = {"item": order}

    if request.method == "POST":
        order.delete()
        return redirect("/")

    return render(request, "accounts/delete.html", context)

