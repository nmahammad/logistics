# views.py
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User, Customer, Order, OrderItem, Transaction, Warehouse
from .serializers import UserSerializer, CustomerSerializer, OrderSerializer, OrderItemSerializer, TransactionSerializer, WarehouseSerializer
import requests
from django.http import HttpResponse  # Adjust the import based on your needs
from django.core.serializers import serialize
from rest_framework import status
from django.shortcuts import render, redirect
from . import forms

def my_view(request):
    # Your view logic here
    # ...

    # Redirect the user to a different URL
    return redirect('some_other_url_name')

# # # # # # # # # # # #    API views # # # # # # # # # # # # 
# User views
@api_view(['GET'])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getUser(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def addUser(request):
    serializer = UserSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)


@api_view(['PUT'])
def updateUser(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(instance=user, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteUser(request, pk):
    user = User.objects.get(id=pk)
    user.delete()
    
    return Response('User successfully deleted!')

# # # # # # # # # # # # # # # # # # # Customer views
@api_view(['GET'])
def getCustomers(request):
    customers = Customer.objects.all()
    serializer = CustomerSerializer(customers, many=True)
    return Response(serializer.data)

@api_view(['GET' ])
def getCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    serializer = CustomerSerializer(customer, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def addCustomer(request):
    serializer = CustomerSerializer(data=request.data)
    
    try:
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['PUT'])
def updateCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    serializer = CustomerSerializer(instance=customer, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    customer.delete()
    
    return Response('Customer successfully deleted!')



# # # # # # # # # # # # # # # # # # # # # # # # # Order views

@api_view(['GET' , 'POST'])
def getOrders(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)

@api_view(['GET' , 'POST'])
def getOrder(request, pk):
    order = Order.objects.get(id=pk)
    serializer = OrderSerializer(order, many=False)
    return Response(serializer.data)

@api_view(['POST' , 'GET'])
def addOrder(request):
    serializer = OrderSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['PUT'])
def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    serializer = OrderSerializer(instance=order, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    order.delete()
    
    return Response('Order successfully deleted!')


# # # # # # # # # # # # # # # # # # # # # # # # # # # # OrderItem views


@api_view(['GET' , 'POST'])
def getOrderItems(request):
    order_items = OrderItem.objects.all()
    serializer = OrderItemSerializer(order_items, many=True)
    return Response(serializer.data)

@api_view(['GET' , 'POST'])
def getOrderItem(request, pk):
    order_item = OrderItem.objects.get(id=pk)
    serializer = OrderItemSerializer(order_item, many=False)
    return Response(serializer.data)

@api_view(['POST' , 'GET'])
def addOrderItem(request):
    serializer = OrderItemSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['PUT'])
def updateOrderItem(request, pk):
    order_item = OrderItem.objects.get(id=pk)
    serializer = OrderItemSerializer(instance=order_item, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteOrderItem(request, pk):
    order_item = OrderItem.objects.get(id=pk)
    order_item.delete()
    
    return Response('OrderItem successfully deleted!')




# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Transaction views

@api_view(['GET' , 'POST'])
def getTransactions(request):
    transactions = Transaction.objects.all()
    serializer = TransactionSerializer(transactions, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getTransaction(request, pk):
    transaction = Transaction.objects.get(id=pk)
    serializer = TransactionSerializer(transaction, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def addTransaction(request):
    serializer = TransactionSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['PUT'])
def updateTransaction(request, pk):
    transaction = Transaction.objects.get(id=pk)
    serializer = TransactionSerializer(instance=transaction, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteTransaction(request, pk):
    transaction = Transaction.objects.get(id=pk)
    transaction.delete()
    
    return Response('Transaction successfully deleted!')



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Warehouse views

@api_view(['GET'])
def getWarehouses(request):
    warehouses = Warehouse.objects.all()
    serializer = WarehouseSerializer(warehouses, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getWarehouse(request, pk):
    warehouse = Warehouse.objects.get(id=pk)
    serializer = WarehouseSerializer(warehouse, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def addWarehouse(request):
    serializer = WarehouseSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['PUT'])
def updateWarehouse(request, pk):
    warehouse = Warehouse.objects.get(id=pk)
    serializer = WarehouseSerializer(instance=warehouse, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteWarehouse(request, pk):
    warehouse = Warehouse.objects.get(id=pk)
    warehouse.delete()
    
    return Response('Warehouse successfully deleted!')



# # # # #  template views # # # # # # # 


def order_search(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')

        try:
            # Fetch the order with the given ID
            order = Order.objects.get(id=order_id)

            # Serialize the order data
            serialized_order = OrderSerializer(order).data

            # Render the template with the order details
            return render(request, 'tracking_display.html', {'order': serialized_order})
        except Order.DoesNotExist:
            return HttpResponse("Order not found", status=404)

    return render(request, 'tracking_search.html')



from django.shortcuts import render, get_object_or_404

def order_details(request, pk):
    try:
        order = get_object_or_404(Order, id=pk)

        # Access the customer name through the related field
        customer_name = order.customer_id.customer_name

        # Add the customer name to the serialized order data
        serialized_order = OrderSerializer(order).data
        serialized_order['customer_name'] = customer_name

        # Render the template with the order details
        return render(request, 'tracking_display.html', {'order': serialized_order})
    except Order.DoesNotExist:
        return HttpResponse("Order not found", status=404)




def success_view(request):
    return render(request, 'success.html')




API_ENDPOINT = 'http://127.0.0.1:8000/api/orders/create/'  # Replace with your actual API endpoint

def create_new_order(request):
    if request.method == 'POST':
        form = forms.OrderForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            form.save()

            # Extract form data
            form_data = form.cleaned_data

            # Make a POST request to the API
            api_data = {
                'sender_name': form_data['sender_name'],
                'sender_address': form_data['sender_address'],
                'sender_email': form_data['sender_email'],
                'sender_phone': form_data['sender_phone'],
                'receiver_name': form_data['receiver_name'],
                'receiver_address': form_data['receiver_address'],
                'receiver_phone': form_data['receiver_phone'],
                'receiver_email': form_data['receiver_email'],
                'origin_address': form_data['origin_address'],
                'destination_address': form_data['destination_address'],
            }

            response = requests.post(API_ENDPOINT, data=api_data)

            # Check the API response
            if response.status_code == 201:  # Assuming 201 is the status code for successful creation
                print("API request successful!")
            else:
                print("API request failed. Status code:", response.status_code)

            return redirect('tracking:success')  # Redirect to the success page after successful form submission

        else:
            # Print errors if the form is not valid
            print("Form errors:", form.errors)
    else:
        form = forms.OrderForm()

    return render(request, 'order.html', {'form': form})
