from django.shortcuts import render
from store.models import Product
from django.views.decorators.csrf import csrf_protect
#from django.views.decorators.http import require_POST

@csrf_protect
#@require_POST

def home(request):
    products = Product.objects.all().filter(is_available=True)

    context = {
        'products' : products,

    }

    return render(request, 'home.html', context)
