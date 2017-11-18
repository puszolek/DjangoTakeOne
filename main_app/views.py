from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    # returning http response
    #return HttpResponse('<h1>Hello everyone!</h1>')

    # now rendering the template
    return render(rewuest, 'index.html')
