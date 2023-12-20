from django.urls import path
from BCimg import views

urlpatterns = [
    path('', views.Home_list, name='home'),
    path('product', views.Product_list, name='product'),
    path('about', views.About_list, name='about'),
    path('register', views.register, name='register'),
    path('login', views.login_page, name='login'),
    path('cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('view_cart', views.view_cart, name='view_cart'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('logout/', views.logout_view, name='logout'),
    path('search/', views.search, name='search'),
    path('addabaya/', views.addabaya, name='addabaya'),
    path('cart/', views.add_to_cart, name='cart'), 
    
]

