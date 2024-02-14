import http
from pydoc import render_doc
from urllib import request
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from ToDoAPP.models import ToDo_table
import json
import requests

def home(request):
    print("This is my first django website")
    return HttpResponse("<h1>Home Page </h1>")
def contact(request):
    return HttpResponse("Contact Page")
def career(request):
    return HttpResponse("Career Page")
def blog(request):
    return HttpResponse("<h1>This is my blog</h1>")
def about_us(request):
    return HttpResponse ("<h1> This is the about us page</h1>")
def welcome(request,name):
    return HttpResponse(f"<h1>We welcome {name} to our page</h1>")
def home(request):
    print('yes your function is working')
    return HttpResponse('''<h1>Home page</h1>  
    <a href="/douala/Bamenda/">Jane</a> 
    <br> <a href="/douala/Doe/">Doe</a>
     <br> <a href="/douala/Toronto/">Toronto</a> 
    <br> <a href="/douala/Brampton/">Brampton</a>
    <br> <a href="/todoapp/">TodoApp</a>''' )
def todo_function(request):
    if request.GET.get("task") != None:
        data = ToDo_table(task_name=request.GET.get("task"))
        data.save()
    print(request.GET.get("task"))
    all_data =ToDo_table.objects.values()[::-1]
    all_data = all_data[:5]
    # print(all_data)
    return render(request, "index.html",{"data":all_data})

def delete_function(request,id):
    print("testing delete", id)
    data = ToDo_table.objects.get(id=id) 
    data.delete()
    return HttpResponseRedirect("/todoapp/")

def weather_function(request):
    output = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=43.731548&lon=-79.7590487&appid=3ed2bc661efb075dc75af44c65fb545a')
    # print (output.json()["main"]["temp"]["humidity"])
    print (output.json()['main']['temp'])
    temp = output.json()['main']['temp']
    print (output.json()['sys']['country'])
    country = output.json()['sys']['country']
    print (output.json()['name'])
    name = output.json()['name']
    print (output.json())
    print("test weather")
    data = {'temp': temp, 'country':country , 'name': name }
    return render(request, 'weatherapp.html', {'data': data})
