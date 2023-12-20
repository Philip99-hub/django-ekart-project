from django.urls import path
from. import views

app_name = "Seller"

urlpatterns = [   
    path('',views.seller_home,name="seller_home"),
    path('product/add',views.add_product,name="add_product"),
    # path('add_category',views.add_category,name="add_category"),
    path('product',views.view_products,name="view_product"),
    # path('view_category',views.view_category,name="view_category"),
    path('profile',views.profile,name="profile"),
    path('myOrders',views.view_orders,name="view_orders"),
    path('stock/update',views.update_stock,name="update_stock"),
    path('order/history',views.order_history,name="order_history"),

   
]