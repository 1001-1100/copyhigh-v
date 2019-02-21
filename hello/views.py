from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

import requests
from bs4 import BeautifulSoup
import argparse
import subprocess
import datetime
import django
import time
from z3 import *

# Create your views here.
def index(request):
    return render(request, "index.html")

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})

def result(request):
    r = request.GET

    return render(request, "result.html", options)