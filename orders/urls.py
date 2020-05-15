from django.urls import path

from . import views

#app_name = 'orders'

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
    path("homepage", views.homepage, name="homepage"),
    path("logout", views.logout_request, name="logout"),
    path("login", views.login_request, name="login"),
    path('order', views.order_request, name="order"),
    path('add', views.add_request, name="add"),
    path('shopping_cart', views.shopping_cart, name="shopping_cart"),
    path('tracker', views.tracker, name="tracker"),
    path('staffpage', views.staffpage, name="staffpage"),
    path('<int:order_id>/order_process', views.order_process, name="order_process")
]
