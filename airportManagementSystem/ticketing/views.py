from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World, You're at the index.")

def detail(request, iD):
    return HttpResponse("You're looking for details for user " + iD)

def book(request):
    return HttpResponse("You're here to book tickets")

def cancel(request, iD):
    return HttpResponse("You're here to cancel tickets for " + iD)
