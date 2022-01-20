from django.core.checks import messages
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import addressForm, customerAdd
from account.models import customer
from .models import Address, Order, OrderItem
from product.models import Product
from cart.cart import Cart


# Create your views here.

def checkout(request):
    addressforms = addressForm(request.POST or None)
    customerForm = customerAdd(request.POST or None)
    if request.method =='POST':
        
        customerobj = customer.objects.create(
            email = request.POST['email'],
            name = request.POST['name'],
            phone_number = request.POST['phone_number'],
        )
        customerobj.save()
        customerinstance = customer.objects.get(id=customerobj.id)
        addressobj = Address(
            address=request.POST['address'],
            appartment=request.POST['appartment'],
            street=request.POST['street'],
            LandMark=request.POST['LandMark']
        )
        
        addressobj.save()

        cart = request.session['cart']
        mylist = []
        for key, value in cart.items():
            id = value['product_id']
            product_instance = Product.objects.get(id=id)
            mylist.append(product_instance.id)
            order_item = OrderItem.objects.create(
                product = product_instance,
                quantity= value['quantity'],
                price=value['price'],
            
            )
            order_item.save()
        
        # myorder = Order(
        #         message= request.POST['notes'],
        #     )
        myorder = Order.objects.create(
            customer = customerinstance,
            message = request.POST['notes'],
        )
        
        print(mylist)
        for x in mylist:
           myorder.item.add(OrderItem.objects.get(id=x))
         
        print(mylist)
        cart = Cart(request)
        cart.clear()
        return HttpResponseRedirect(reverse('confirm'))
        
        return HttpResponse("end point reached")
    

    context = {
        'address' : addressforms,
        'customer' : customerForm,
    }

    return render(request, 'frontend/checkout.html', context)


def check(request):
    cart = request.session['cart']
    mycart = cart.items()
    for key, value in mycart:
        print(value["quantity"])


    return HttpResponse(cart)




    # order_obj = Order(
    #             item = product_instance,
    #             address= Address.objects.get(addressobj.id),
    #             quantity= value['quantity'],
    #             message= request.POST['notes'],
    #             price=value['price'],
    #         )