from django.shortcuts import render,HttpResponse
from shop101.models import Product

# Create your views here.
def test(request):
    return HttpResponse('Hi india')


def home(request):
    products = Product.objects.all()
    # print('Our Offerings')
    return render(request, 'product_list.html',context={'product_list':products})

def mycart(request):
    cartItems = Cart.objects.all()
    return render(request, 'cartItem.html',context = { 'cartItem' : cartItems})

def show_product(request,id):
    p_id = id
    product = Product.objects.get(id= p_id)
    return render(request , 'show_product.html',context = { 'product' : product })
