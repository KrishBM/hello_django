from django.shortcuts import render,HttpResponse
from home.models import Contact
from datetime import datetime
from django.contrib import messages
# Create your views here.
def index(request):
    context={
        'variable1':'11111 this is my page bro....!!!',
        'variable2':'22222 this is my page bro....!!!'
    }
    return render(request,'index.html',context)
def about_us(request):
    return render(request,'about_us.html')
def contact_us(request):
    if request.method=='POST':
        name=request.POST.get('name2')
        email=request.POST.get('email2')
        mobile=request.POST.get('mobile2')
        desc=request.POST.get('desc2')
        contact_us1=Contact(name=name,email=email,mobile=mobile,desc=desc,date=datetime.today())
        contact_us1.save()
        messages.success(request, 'Contact detail submited...!')
    return render(request,'contact_us.html')
