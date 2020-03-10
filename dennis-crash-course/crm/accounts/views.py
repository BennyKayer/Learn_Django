from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# Local
from .models import Customer, Product, Order
from .forms import OrderForm, CreateUserForm
from .filters import OrderFilter
from .decorators import unauthenticated_user, allowed_users, admin_only

# Create your views here.


@unauthenticated_user
def registerPage(req):
    # if req.user.is_authenticated:
    #     return redirect("home")

    form = CreateUserForm()

    if req.method == "POST":
        form = CreateUserForm(req.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")

            group = Group.objects.get(name="customer")
            user.groups.add(group)

            messages.success(req, f"Account was created for {username}")

            return redirect("login")

    context = {"form": form}
    return render(req, "accounts/register.html", context)


@unauthenticated_user
def loginPage(req):
    # if req.user.is_authenticated:
    #     return redirect("home")

    if req.method == "POST":
        username = req.POST.get("username")
        password = req.POST.get("password")

        user = authenticate(request=req, username=username, password=password)

        if user is not None:
            login(request=req, user=user)
            return redirect("home")
        else:
            messages.error(req, message="Username or password incorrect")

    context = {}
    return render(req, "accounts/login.html", context)


def userPage(request):
    context = {}
    return render(request, "accounts/user.html", context)


def logoutUser(req):
    logout(req)
    return redirect("login")


@login_required(login_url="login")
@admin_only
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


@allowed_users(allowed_roles=["admin"])
@login_required(login_url="login")
def products(req):
    products = Product.objects.all()
    return render(req, "accounts/products.html", {"products": products})


@allowed_users(allowed_roles=["admin"])
@login_required(login_url="login")
def customer(req, pk):
    customer = Customer.objects.get(id=pk)

    orders = customer.order_set.all()
    order_count = orders.count()

    myFilter = OrderFilter(req.GET, queryset=orders)
    orders = myFilter.qs

    context = {
        "customer": customer,
        "orders": orders,
        "order_count": order_count,
        "myFilter": myFilter,
    }
    return render(req, "accounts/customer.html", context)


@allowed_users(allowed_roles=["admin"])
@login_required(login_url="login")
def createOrder(request, pk):
    OrderFormSet = inlineformset_factory(
        Customer, Order, fields=("product", "status"), extra=10
    )
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(instance=customer, queryset=Order.objects.none())
    # form = OrderForm(initial={"customer": customer})
    if request.method == "POST":
        # print("Printing POST", request.POST)
        # form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect("/")

    context = {"formset": formset}

    return render(request, "accounts/order_form.html", context)


@allowed_users(allowed_roles=["admin"])
@login_required(login_url="login")
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


@allowed_users(allowed_roles=["admin"])
@login_required(login_url="login")
def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    context = {"item": order}

    if request.method == "POST":
        order.delete()
        return redirect("/")

    return render(request, "accounts/delete.html", context)

