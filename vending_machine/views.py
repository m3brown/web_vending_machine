from django.shortcuts import render
from django.http import JsonResponse
from vending_machine import VendingMachine

# Create your views here.
vm = VendingMachine()

def index(request):
    vm = VendingMachine()
    return render(request, 'vending_machine/index.html', {'msg': vm.message})

def insert_coin(request):
    vm.insert_coin(1)
    return JsonResponse({'msg': vm.message})

def buy_product(request):
    try:
        vm.buy_product()
        return JsonResponse({'msg': vm.message, 'product': "product"})
    except RuntimeError as e:
        return JsonResponse({'msg': e.message, 'product': None})
