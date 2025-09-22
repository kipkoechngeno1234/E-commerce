from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def a_tech(request):
    return render(request, 'login.html')