from django.shortcuts import render
from django.http import JsonResponse
from vending_machine import VendingMachine

# Create your views here.

def index(request):
    vm = VendingMachine()
    vm.reset()
    return render(request, 'vending_machine/index.html', {'msg': vm.message})

def insert_coin(request):
    vm = VendingMachine()
    vm.insert_coin(1)
    return JsonResponse({'msg': vm.message})

def buy_product(request):
    vm = VendingMachine()
    try:
        vm.buy_product()
        return JsonResponse({'msg': vm.message, 'product': "product"})
    except RuntimeError as e:
        return JsonResponse({'msg': e.message, 'product': None})
