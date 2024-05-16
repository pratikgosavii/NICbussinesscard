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



import hashlib
import base64

def generate_key_from_id(instance_id):
    # Generate a unique key using a hash function
    hash_object = hashlib.sha256(str(instance_id).encode())
    # Encode the hash in base64 to get a 64-character string
    unique_key = base64.urlsafe_b64encode(hash_object.digest()).decode()[:64]
    return unique_key



@login_required(login_url='login')
def add_client(request):

    if request.method == 'POST':

        forms = client_Form(request.POST, request.FILES)

        if forms.is_valid():
            
            new_record = forms.save(commit=False)
            
            # Save the record to get the unique ID
            new_record.save()

            # Generate a unique key based on the new record's ID
            unique_key = generate_key_from_id(new_record.id)

            # Update the record with the generated key
            new_record.random_key = unique_key
            new_record.save()

            return redirect('list_client')
        else:
            print(forms.errors)
    
    else:

        forms = client_Form()

        context = {
            'form': forms
        }
        return render(request, 'add_client.html', context)

        
import copy

@login_required(login_url='login')
def update_client(request, random_key_value):

    instance = client.objects.get(random_key=random_key_value)
    instance_copy = copy.copy(instance)
    if request.method == 'POST':
        form = client_Form(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            updated_client = form.save(commit=False)
            updated_client.random_key = instance_copy.random_key  # Preserve the existing key
            updated_client.save()
            return redirect('list_client')
        else:
            print(form.errors)
    else:
        form = client_Form(instance=instance)

    context = {
        'form': form
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


def show_card(request, random_key_value):

    data = client.objects.get(random_key=random_key_value)

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