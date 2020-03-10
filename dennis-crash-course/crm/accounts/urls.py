from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    # Authentication
    path("register/", views.registerPage, name="register"),
    path("login/", view=views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("user/", view=views.userPage, name="user-page"),
    # Customers
    path("products/", views.products, name="products"),
    path("customer/<str:pk>", views.customer, name="customer"),
    path("create_order/<str:pk>/", views.createOrder, name="create_order"),
    path("update_order/<str:pk>/", views.updateOrder, name="update_order"),
    path("delete/<str:pk>/", views.deleteOrder, name="delete_order"),
]
