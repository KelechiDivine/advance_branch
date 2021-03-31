from django.shortcuts import render


# Create your views here.

def store(request):
    context = {

    }
    return render(request, 'Drive_app_Html/store.html', context)


def cart(request):
    context = {

    }
    return render(request, 'Drive_app_Html/cart.html', context)


def checkout(request):
    context = {

    }
    return render(request, 'Drive_app_Html/checkout.html', context)
