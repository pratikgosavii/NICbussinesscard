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



def home(request):

    return render(request, 'index.html')

def privacy_policy(request):

    return render(request, 'privacy_policy.html')

def contact_us(request):

    return render(request, 'contact.html')


def about_us(request):

    return render(request, 'about_us.html')

        
import copy


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

        


from django.http import HttpResponse
import qrcode
from io import BytesIO
from django.core.files.base import ContentFile
import base64




def print_single_qr(request, client_id):

    a = client.objects.get(id = client_id)


    qr_size = 600

    box_size = qr_size // 4  # You can experiment with different values

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=box_size,
        border=0,
    )
    qr.add_data("https://www.nfcmetalcard.com/showcard/" + a.random_key)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    qr_code_image = base64.b64encode(buffer.getvalue()).decode()


    return render(request, 'html_qr_single.html', {'data' : qr_code_image})


def delete_client(request, client_id):

    client.objects.get(id=client_id).delete()

    return HttpResponseRedirect(reverse('list_client'))



def list_client(request):

    data = client.objects.all()
    context = {
        'data': data
    }
    return render(request, 'list_client.html', context)



def add_demo(request):

    if request.method == 'POST':

        forms = demo_Form(request.POST)

        if forms.is_valid():
            
           
            forms.save()
        
            return redirect('list_demo')
        
        else:
            print(forms.errors)
    
    else:

        forms = demo_Form()

        context = {
            'form': forms
        }
        return render(request, 'add_demo.html', context)





def list_demo(request,):

    data = demo.objects.all()

    context = {
        'data': data
    }

    return render(request, 'list_demo.html', context)




# def add_payment(request):

#     if request.method == 'POST':


def add_payment(request, demo_id):

    demo_instance = demo.objects.get(id = demo_id)

    if request.method == 'POST':


            
        updated_request = request.POST.copy()
        updated_request.update({'demo': demo_instance.id})

        forms = payment_Form(updated_request)

        if forms.is_valid():
            
           
            forms.save()
        
            url = reverse('add_payment', args=[demo_instance.id])
        
            return redirect(url)
        
        else:
            print(forms.errors)
    
    else:

        forms = payment_Form()

        data = payment.objects.filter(demo = demo_instance)

        total_paid = data.aggregate(Sum('amount'))['amount__sum'] or 0
        remaining_amount = demo_instance.amount - int(total_paid)

        context = {
            'form': forms,
            'data': data,
            'demo_instance' : demo_instance,
            'total_paid' : total_paid,
            'remaining_amount' : remaining_amount,
        }
        return render(request, 'add_payment.html', context)
    


def update_payment(request, payment_id):

    payment_instance = payment.objects.get(id = payment_id)

    if request.method == 'POST':


            
        updated_request = request.POST.copy()
        updated_request.update({'demo': payment_instance.demo.id})

        forms = payment_Form(updated_request, instance = payment_instance)

        if forms.is_valid():
            
           
            forms.save()

            url = reverse('add_payment', args=[payment_instance.demo.id])
        
            return redirect(url)
        
        else:
            print(forms.errors)
    
    else:

        forms = payment_Form(instance = payment_instance)

        context = {
            'form': forms,
        }
        return render(request, 'update_payment.html', context)




def delete_payment(request, payment_id):

    data = payment.objects.get(id = payment_id)
    data_copy = copy.copy(data)
    data.delete()

    context = {
        'data': data
    }

    url = reverse('add_payment', args=[data_copy.demo.id])
        
    return redirect(url)



def show_card(request, random_key_value):

    data = client.objects.get(random_key=random_key_value)

    context = {
        'data': data
    }

    return render(request, 'card.html', context)



def dashboard(request):

    data = client.objects.all().count

    context = {
        'data': data
    }
    return render(request, 'dashboard.html', context)