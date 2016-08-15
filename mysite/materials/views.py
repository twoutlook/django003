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
        context = {'customer_list': {}}
        return render(request, 'materials/index.html', context)     
        
    customer_list = Customer.objects.order_by('field1')[:100]
    context = {'customer_list': customer_list}
    return render(request, 'materials/index.html', context)     
    
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)