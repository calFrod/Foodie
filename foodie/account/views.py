from django.shortcuts import render

# Create your views here.
def register(request):
    context = {}
    return render(request, 'account/register.html', context)

def login(request):
    context = {}
    return render(request, 'account/login.html', context)