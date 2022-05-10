from django.shortcuts import redirect, render
from random import randint
from mainapp.models import *

# Create your views here.
def index(request):
    district=District.objects.all()
    typ=PropertyType.objects.all()
    vtype=Vtype.objects.all()
    prop=Property.objects.filter(premium=True)
    return render(request, 'index.html',{'dist':district,'typ':typ,'vtyp':vtype,'prop':prop})

def saleform(request):
    dist=request.POST.get('district')
    typ=request.POST.get('proptype')
    return redirect('/sales/'+dist+'/'+typ)

def sales(request,district,type):
    prop=Property.objects.filter(district=district,property_type=type,purpose__name='Sale')
    return render(request, 'property-grid.html',{'prop':prop,'title':'Sale'})

def rentform(request):
    dist=request.POST.get('district')
    typ=request.POST.get('proptype')
    return redirect('/rent/'+dist+'/'+typ)

def rent(request,district,type):
    prop=Property.objects.filter(district=district,property_type=type,purpose__name='Rent')
    return render(request, 'property-grid.html',{'prop':prop,'title':'Rent'})

def vehcform(request):
    dist=request.POST.get('district')
    typ=request.POST.get('vtype')
    return redirect('/vehicle/'+dist+'/'+typ)

def vehicle(request,district,type):
    prop=Vehichle.objects.filter(district=district,vehichle_type=type)
    return render(request, 'property-grid.html',{'prop':prop,'title':'Vehicle'})

def prodetail(request,id):
    prop=Property.objects.get(id=id)
    return render(request, 'property-detail.html',{'prop':prop,'title':'Property'})

def vehdetail(request,id):
    prop=Vehichle.objects.get(id=id)
    return render(request, 'property-detail.html',{'prop':prop,'title':'Vehicle'})

def about(request):
    prop=Property.objects.filter(premium=True)
    print((prop))
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')