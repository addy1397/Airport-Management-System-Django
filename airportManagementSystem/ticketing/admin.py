from __future__ import unicode_literals
from django.contrib import admin

from .models import Person, Ticket

admin.site.register(Person)
admin.site.register(Ticket)
