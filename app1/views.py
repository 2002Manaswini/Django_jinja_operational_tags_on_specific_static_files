from django.shortcuts import render

# Create your views here.

def taylor(request):
    return render(request,'taylor.html')