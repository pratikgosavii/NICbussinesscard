from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *


from .models import *
from django.db.models import Sum

from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *
from .models import *

from datetime import date

from datetime import datetime
from django.urls import reverse
from django.http.response import HttpResponseRedirect, JsonResponse
from django.contrib import messages



@login_required(login_url='login')
def add_client(request):

    if request.method == 'POST':

        forms = client_Form(request.POST, request.FILES)

        if forms.is_valid():
            forms.save()
            return redirect('list_client')
        else:
            print(forms.errors)
    
    else:

        forms = client_Form()

        context = {
            'form': forms
        }
        return render(request, 'add_client.html', context)

        

@login_required(login_url='login')
def update_client(request, client_id):

    if request.method == 'POST':

        instance = client.objects.get(id=client_id)

        forms = client_Form(request.POST, request.FILES, instance=instance)

        if forms.is_valid():
            forms.save()
            return redirect('list_client')
        else:
            print(forms.errors)
    
    else:

        instance = client.objects.get(id=client_id)
        forms = client_Form(instance=instance)

        context = {
            'form': forms
        }
        return render(request, 'add_client.html', context)

        

@login_required(login_url='login')
def delete_client(request, client_id):

    client.objects.get(id=client_id).delete()

    return HttpResponseRedirect(reverse('list_client'))


@login_required(login_url='login')
def list_client(request):

    data = client.objects.all()
    context = {
        'data': data
    }
    return render(request, 'list_client.html', context)


def show_card(request, user_id):

    data = client.objects.get(id=user_id)

    context = {
        'data': data
    }

    return render(request, 'card.html', context)


@login_required(login_url='login')
def dashboard(request):

    data = client.objects.all().count

    context = {
        'data': data
    }
    return render(request, 'dashboard.html', context)