from django.shortcuts import render
from django.http import HttpResponse
from family_members.models import Family_members

# Create your views here.

def create_family_member(request):
    new_family_member = Family_members.objects.create(name="John Doe", age = 20, alive = True)
    return HttpResponse("se creo el nuevo familiar")

def list_familiars(request):
    all_family = Family_members.objects.all()
    print(all_family)
    context = { 
        "all_family": all_family,
    }
    return render(request, "list_familiars.html", context=context)