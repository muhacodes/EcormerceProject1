from django.core.checks import messages
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import addressForm, customerAdd
from account.models import customer
from .models import Address, Order, OrderItem
from product.models import Product
from cart.cart import Cart
from django.core.mail import send_mail
from django.template import context
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage
from datetime import date, timedelta


# Create your views here.

def checkout(request):
    addressforms = addressForm(request.POST or None)
    customerForm = customerAdd(request.POST or None)
    if request.method =='POST':

        #  some variable names
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone_number']
        
        customerobj = customer.objects.create(
            email = email,
            name = name,
            phone_number = phone
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
        Cart = {

        }

        if( 'cart' in request.session):
            cart = request.session['cart']
        else:
            return HttpResponseRedirect(reverse('cart:index'))

        mylist = []
        for key, value in cart.items():
            id = value['product_id']
            product_instance = Product.objects.get(id=id)
            
            order_item = OrderItem.objects.create(
                product = product_instance,
                quantity= value['quantity'],
                price=value['price'],
            
            )
            product_instance.quantity = product_instance.quantity - order_item.quantity
            product_instance.save()
            order_item.save()
            mylist.append(order_item.id)

        
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
         
        # print(mylist)
        # ob = OrderItem.objects.get(id=1)
        # return HttpResponse(mylist)
        # cart = Cart(request)
        # cart.clear()
        del request.session['cart']

        # subject = 'Thank you for registering to our site'
        # message = 'first message hoss'
        # email_from = 'muhacodes@gmail.com'
        # recipient_list = ['muha.oq3@gmail.com',]

        # send_mail( subject, message, email_from, recipient_list )
        
        current = date.today()

        EstimatedDeliveryDate = current + timedelta(days=1)
        ctx = {
        'Name': request.POST['name'],
        'order_id' :myorder.order_id,
        'deliveryDate' :EstimatedDeliveryDate
        
        }
        message = get_template('mail.html').render(ctx)
        msg = EmailMessage(
            'Order Confirmation',
            message,
            'muhacodes@gmail.com',
            [request.POST['email']],
        )
        msg.content_subtype ="html"# Main content is now text/html
        msg.send()
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