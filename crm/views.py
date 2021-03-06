from django.shortcuts import render
from .models import Order
from .forms import OrderForm

# Create your views here.


def first_page(request):
    object_list = Order.objects.all()
    form = OrderForm(request.POST)
    return render(request, './index.html', {'object_list': object_list,
                                            'form': form})


def thx_page(request):
    name = request.POST['name']
    phone = request.POST['phone']
    element = Order(order_name=name, order_phone=phone)
    element.save()
    return render(request, './thx_page.html')
