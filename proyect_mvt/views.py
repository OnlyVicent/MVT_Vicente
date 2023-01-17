from django.http import HttpResponse
from django.shortcuts import render

def hola_mundo(request):
    return HttpResponse("Hola Mundo")

def vista_template(request):
    return render(request, "template.html", context={})