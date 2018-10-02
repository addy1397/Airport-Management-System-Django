from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Person,Ticket

def index(request):
    return render(request, 'ticketing/index.html')

def detail(request, iD):
    try:
        person = Person.objects.get(iD=iD)
    except Person.DoesNotExist:
        return render(request, 'ticketing/doesNotExist')
    return render(request, 'ticketing/detail.html', {'person': person})

def ticket(request, iD):
    try:
        tickets = Ticket.objects.filter(person=iD)
    except Ticket.DoesNotExist:
        return render(request, 'ticketing/doesNotExist')
    return render(request, 'ticketing/ticket.html', {'ticket':tickets})

def confirm(request, start, des, id):
    ticket=Ticket(startingPoint=start, destination=des, person=Person.objects.get(iD=id), time="00:00")
    ticket.save()
    return render(request, 'ticketing/confirmed.html', {'id':id})

def book(request):
    return render(request, 'ticketing/book.html')

def cancel(request, iD):
    tempTicket = Ticket.objects.filter(id=iD)
    tempTicket.delete()
    return render(request, 'ticketing/cancel.html')
