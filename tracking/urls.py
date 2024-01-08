from django.urls import path
from . import views
app_name = "tracking"

urlpatterns = [
    # User URLs
    path('api/users/', views.getUsers),
    path('api/users/create/', views.addUser),
    path('api/users/read/<str:pk>/', views.getUser),
    path('api/users/update/<str:pk>/', views.updateUser),
    path('api/users/delete/<str:pk>/', views.deleteUser),

    # Customer URLs
    path('api/customers/', views.getCustomers),
    path('api/customers/create/', views.addCustomer),
    path('api/customers/read/<str:pk>/', views.getCustomer),
    path('api/customers/update/<str:pk>/', views.updateCustomer),
    path('api/customers/delete/<str:pk>/', views.deleteCustomer),

    # Order URLs
    path('api/orders/', views.getOrders),
    path('api/orders/create/', views.addOrder),
    path('api/orders/read/<str:pk>/', views.getOrder),
    path('api/orders/update/<str:pk>/', views.updateOrder),
    path('api/orders/delete/<str:pk>/', views.deleteOrder),

    # OrderItem URLs
    path('api/order-items/', views.getOrderItems),
    path('api/order-items/create/', views.addOrderItem),
    path('api/order-items/read/<str:pk>/', views.getOrderItem),
    path('api/order-items/update/<str:pk>/', views.updateOrderItem),
    path('api/order-items/delete/<str:pk>/', views.deleteOrderItem),

    # Transaction URLs
    path('api/transactions/', views.getTransactions),
    path('api/transactions/create/', views.addTransaction),
    path('api/transactions/read/<str:pk>/', views.getTransaction),
    path('api/transactions/update/<str:pk>/', views.updateTransaction),
    path('api/transactions/delete/<str:pk>/', views.deleteTransaction),

    # Warehouse URLs
    path('api/warehouses/', views.getWarehouses),
    path('api/warehouses/create/', views.addWarehouse),
    path('api/warehouses/read/<str:pk>/', views.getWarehouse),
    path('api/warehouses/update/<str:pk>/', views.updateWarehouse),
    path('api/warehouses/delete/<str:pk>/', views.deleteWarehouse),

    # # Template urls
    path('orders/search/', views.order_search, name='order_search'),
    path('orders/<str:pk>/', views.order_details, name='order_details'),
    path('create_order/', views.create_new_order, name='create_new_order'),
    path('order_success/', views.success_view, name='success'),  # Add a new URL for the success page

]
