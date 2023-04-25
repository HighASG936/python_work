from django.shortcuts import render
from .models import Pizza

def index(request):
    """The home page of pizzeria"""
    return render(request, 'pizzas/index.html')

def type_pizzas(request):
    """Show all types pf pizzas availale"""
    names = Pizza.objects.order_by('id')
    context = {'types': names}
    return render(request, 'pizzas/names.html', context)

def toppings(request, name_id):
    """show topping for each type of pizza"""
    name = Pizza.objects.get(id=name_id)
    toppings = name.topping_set.order_by('id')
    context = {'name': name, 'toppings': toppings}
    return render(request, 'pizzas/toppings.html', context)


