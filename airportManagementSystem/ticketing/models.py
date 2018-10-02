from __future__ import unicode_literals

from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=50)
    nationality = models.CharField(max_length=30)
    iD = models.CharField(primary_key=True, max_length=20)
    creditCard = models.CharField(max_length=20)

    def __str__(self):
        return self.iD

class Ticket(models.Model):
    startingPoint = models.CharField(max_length=20)
    destination = models.CharField(max_length=20)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    time = models.CharField(max_length=10)
    price = models.IntegerField(default = 1000)

    def __str__(self):
        return self.person.iD + " " + self.time + " " + self.startingPoint + " " + self.destination
