from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    context={
        'variable1':'11111 this is my page bro....!!!',
        'variable2':'22222 this is my page bro....!!!'
    }
    return render(request,'index.html',context)
def about(request):
    return HttpResponse('this is about page')
def about1(request):
    return HttpResponse('this is about1 page')