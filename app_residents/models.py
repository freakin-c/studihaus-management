from django.db import models
from datetime import date, timedelta

class Resident(models.Model):

    forename = models.CharField('Forename', max_length=255)
    surname = models.CharField('Surname', max_length=255)
    email = models.EmailField('E-Mail')
    mobile_number = models.CharField('Mobile number', max_length=20, blank=True)
    date_move_in = models.DateField('Date of move-in', help_text='Date of move-in like on rental agreement', default=date.today)
    date_move_out = models.DateField('Date of move-out', help_text='Date of move-out', null=True, blank=True)

    def __str__(self):
        return self.forename

class Room(models.Model):
    room_code = models.CharField('Room code', help_text='Room code like "HH32"', max_length=4, unique=True)
    rent = models.DecimalField('Rent', max_digits=5, decimal_places=2)
    resident = models.OneToOneField(Resident, on_delete=models.PROTECT, related_name='room', null=True, blank=True)

    def __str__(self):
        return self.room_code + (f' ({self.resident})' if self.resident else '')

