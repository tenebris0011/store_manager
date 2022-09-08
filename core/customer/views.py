from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse

from .forms import PreOrderForm, StoreCreditForm
from .models import StoreCredit as StoreCreditModel
from .models import PreOrder as PreOrderModel

def StoreCredit(request):
    if request.user.is_authenticated:
        if request.POST.get('delete'):
            item = StoreCreditModel.objects.get(id=request.POST.get('id'))
            item.delete()
        
        elif request.method == "POST":
            try:
                instance = StoreCreditModel.objects.get(id=request.POST.get('id'))
            except StoreCreditModel.DoesNotExist:
                instance = None
            except ValueError:
                instance = None
            form = StoreCreditForm(request.POST, instance=instance)
            if form.is_valid():
                item = form.save(commit=False)
                item.user = request.user
                item.save()
                return redirect("customer:store_credit")
        form = StoreCreditForm()
        credit = request.user.store_credit.all().order_by('-date_added')
        template = loader.get_template('customer/storecredit.html')
        context = {
            'store_credit': credit,
            'form': form,
        }
        return HttpResponse(template.render(context, request))
    return HttpResponse("Please login.")

def PreOrders(request):
    if request.user.is_authenticated:
        if request.POST.get('delete'): 
            item = PreOrderModel.objects.get(id=request.POST.get('id'))
            item.delete()
        elif request.method == "POST":
            try: 
                instance = PreOrderModel.objects.get(id=request.POST.get('id'))
            except PreOrderModel.DoesNotExist:
                instance = None
            except ValueError:
                instance = None
            form = PreOrderForm(request.POST, instance=instance)
            if form.is_valid():
                item = form.save(commit=False)
                item.user = request.user
                item.save()
                return redirect("customer:preorders")
        form = PreOrderForm()
        preorders = request.user.pre_orders.all().order_by('-date_added')
        template = loader.get_template('customer/preorders.html')
        context = {
            'preorders': preorders,
            'form': form,
        }
        return HttpResponse(template.render(context, request))
    return HttpResponse("Please login.")
    