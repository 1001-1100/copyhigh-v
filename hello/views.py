from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Greeting
from .models import invEntry

import datetime
import django
import time

# Create your views here.
def index(request):
    data = {}
    data['employee'] = 111100
    return render(request, "index.html", data)

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})

@csrf_exempt
def addInvEntry(request):
    r = request.POST
    print(r)

    inventry = invEntry(
        item=r.get('item'),
        employee=r.get('employee'),
        beginv=r.get('beginv'),
        endinv=r.get('endinv'),
        actualinv=r.get('actualinv'),
        delivery=r.get('delivery'),
        sales=r.get('sales'),
        salesamount=r.get('salesamount'),
        shortage=r.get('shortage'),
        shortageamount=r.get('shortageamount')
    )
    inventry.save()

    print(inventry)

    return render(request, "result.html")
