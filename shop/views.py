from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
from math import ceil

def index(request):
    products=Product.objects.all()
    print(products)
    n=len(products)
    nSlides=n//4 + ceil((n/4)-(n//4))
    params = {'no of slides': nSlides,'range':range(nSlides),'product':products}
    return render(request, 'shop/index.html',params)

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    return HttpResponse("we are at shop contact")

def tracker(request):
    return HttpResponse("we are at shop tracker")

def search(request):
    return HttpResponse("we are at shop search")

def productview(request):
    return HttpResponse("we are at shop product")

def checkout(request):
    return HttpResponse("we are at shop checkout")