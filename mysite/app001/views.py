from django.http import HttpResponse
from django.http import Http404
from django.template import loader

from django.shortcuts import render
from .models import Customer
from django.conf import settings
from django.shortcuts import redirect
# def index(request):
#     return HttpResponse("Hello, world. 欠料")
    
    
def index(request):
    if not request.user.is_authenticated:
        # return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
        #return redirect('../admin')
        context = {'page_title':'xxx','customer_list': {}}
        return render(request, 'app001/index.html', context)     
        
    customer_list = Customer.objects.order_by('field1')[:100]
    context = {'page_title':'yyy','customer_list': customer_list}
    return render(request, 'app001/index.html', context)     
    
def item001(request):
    if not request.user.is_authenticated:
        # return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
        #return redirect('../admin')
        context = {'page_title':'xxx','customer_list': {}}
        return render(request, 'app001/index.html', context)     
        
    customer_list = Customer.objects.order_by('field1')[:100]
    context = {'page_title':'yyy','customer_list': customer_list}
    return render(request, 'app001/index.html', context)     
    
def item002(request):
    if not request.user.is_authenticated:
        # return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
        #return redirect('../admin')
        context = {'page_title':'xxx','customer_list': {}}
        return render(request, 'app001/index.html', context)     
        
    customer_list = Customer.objects.order_by('field1')[:100]
    context = {'page_title':'yyy','customer_list': customer_list}
    return render(request, 'app001/index.html', context)     
def item003(request):
    if not request.user.is_authenticated:
        # return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
        #return redirect('../admin')
        context = {'page_title':'xxx','customer_list': {}}
        return render(request, 'app001/index.html', context)     
        
    customer_list = Customer.objects.order_by('field1')[:100]
    context = {'page_title':'yyy','customer_list': customer_list}
    return render(request, 'app001/index.html', context)     
def item004(request):
    if not request.user.is_authenticated:
        # return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
        #return redirect('../admin')
        context = {'page_title':'xxx','customer_list': {}}
        return render(request, 'app001/index.html', context)     
        
    customer_list = Customer.objects.order_by('field1')[:100]
    context = {'page_title':'yyy','customer_list': customer_list}
    return render(request, 'app001/index.html', context)     
    