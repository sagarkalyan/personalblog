from django.shortcuts import render, get_object_or_404
from .models import myapp

# Create your views here.
def index(request):
    myapps=myapp.objects
    return render(request, 'myapp/index.html',{'myapps':myapps})

def detail(request, myapp_id):
    myapp_detail=get_object_or_404(myapp, pk=myapp_id)
    return render(request,'myapp/detail.html',{'myapp':myapp_detail})