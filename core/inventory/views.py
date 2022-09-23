from wsgiref.util import request_uri
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from .models import NewInventory as NewInventoryModel
from .models import SinglesInventory as SinglesInventoryModel
from django.views.decorators.http import require_http_methods
from .forms import *


# Create your views here.
@require_http_methods(["GET", "POST"])
def NewInventory(request):
    if request.user.is_authenticated:
        if request.POST.get('delete'):
            item = NewInventoryModel.objects.get(id=request.POST.get('id'))
            item.delete()
        elif request.method == "POST":
            try:
                instance = NewInventoryModel.objects.get(id=request.POST.get('id'))
            except NewInventoryModel.DoesNotExist:
                instance = None
            except ValueError:
                instance = None
            form = NewForm(request.POST, instance=instance)
            if form.is_valid():
                item = form.save(commit=False)
                item.user = request.user
                item.save()
                return redirect("inventory:new")
        form = NewForm()
        new_inventory = request.user.new_inventory.all().order_by('-date_added')
        template = loader.get_template('inventory/new_inventory.html')
        context = {
            'new_inventory': new_inventory,
            'form': form,
        }
        return HttpResponse(template.render(context, request))
    return redirect("/")

@require_http_methods(["GET", "POST"])
def SinglesInventory(request):
    if request.user.is_authenticated:
        if request.POST.get('delete'):
            item = SinglesInventoryModel.objects.get(id=request.POST.get('id'))
            item.delete()

        elif request.method == "POST":
            try:
                instance = SinglesInventoryModel.objects.get(id=request.POST.get('id'))
            except SinglesInventoryModel.DoesNotExist:
                instance = None
            except ValueError:
                instance = None
            form = SinglesForm(request.POST, instance=instance)
            if form.is_valid():
                item = form.save(commit=False)
                item.user = request.user
                item.save()
                return redirect("inventory:singles")
        form = SinglesForm()
        singles_inventory = request.user.singles_inventory.all().order_by('-date_added')
        template = loader.get_template('inventory/singles_inventory.html')
        context = {
            'singles_inventory': singles_inventory,
            'form': form,
        }
        return HttpResponse(template.render(context, request))
    return redirect("/")