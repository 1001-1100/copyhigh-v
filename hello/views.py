from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Greeting
from .models import invEntry
from .models import invItem

import datetime
import django
import time

# Create your views here.

def getlogin(request):
    return render(request, "login.html")

def postlogin(request):
    r = request.POST
    request.session['employee'] = r.get('employee')
    return redirect('/')

def logout(request):
    del request.session['employee']
    return redirect('/login')

def index(request):
    return redirect('/add')

def addpage(request):
    if(request.session.get('employee')):
        invItemList = invItem.objects.all()
        data = {}
        data['employee'] = request.session.get('employee') 
        data['currentDate'] = datetime.datetime.now()
        data['invItems'] = [i.item for i in invItemList.iterator()]
        data['invPrices'] = [i.price for i in invItemList.iterator()]
        data['invBegin'] = [i.inv for i in invItemList.iterator()]

        return render(request, "index.html", data)
    else:
        return redirect('/login')
        
    

def viewpage(request):
    if(request.session.get('employee')):
        invEntryList = invEntry.objects.all().order_by('-date')
        data = {}
        data['employee'] = request.session.get('employee') 
        data['currentDate'] = datetime.datetime.now()
        data['invEntry'] = [i for i in invEntryList.iterator()]
        return render(request, "view.html", data)
    else:
        return redirect('/login')


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
        delivery=r.get('delivery'),
        beginv=r.get('beginv'),
        endinv=r.get('endinv'),
        sales=r.get('sales'),
        salesamount=r.get('salesamount'),
        actualinv=r.get('actualinv'),
        shortage=r.get('shortage'),
        shortageamount=r.get('shortageamount')
    )
    inventry.save()

    if(r.get('actualinv')):
        invItem.objects.filter(item=r.get('item')).update(inv=r.get('actualinv'))
    else:
        invItem.objects.filter(item=r.get('item')).update(inv=r.get('endinv'))

    print(inventry)

    return redirect('/')
