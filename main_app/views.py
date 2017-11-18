from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

class Person:
    def __init__(self, name, age, location, food):
        self.name = name
        self.age = age
        self.location = location
        self.food = food

people = [Person('Paula', 23, 'Warsaw', 'pizza'), Person('Mateusz', 23, 'Warsaw', 'spaghetti')]

def index(request):

    #name = "Paula"
    #age = 23
    #context = {'my_name': name, 'my_age': age}

    # returning http response
    #return HttpResponse('<h1>Hello everyone!</h1>')

    # now rendering the template
    return render(request, 'index.html', {'people': people})
