from django.db import models
from django.utils.translation import gettext as _

from datetime import date, timedelta

class Resident(models.Model):

    forename = models.CharField(_('Forename'), max_length=255)
    surname = models.CharField(_('Surname'), max_length=255)
    email = models.EmailField(_('E-Mail'))
    mobile_number = models.CharField(_('Mobile number'), max_length=20, blank=True)
    date_move_in = models.DateField(_('Date of move-in'), help_text=_('Date of move-in like stated on rental agreement'), default=date.today)
    date_move_out = models.DateField(_('Date of move-out'), help_text=_('Date of move-out'), null=True, blank=True)

    def __str__(self):
        return self.forename

    class Meta:
        verbose_name = _('Resident')
        verbose_name_plural = _('Residents')

class Room(models.Model):
    room_code = models.CharField(_('Room code'), help_text=_('Room code like "HH32"'), max_length=4, unique=True)
    rent = models.DecimalField(_('Rent'), max_digits=5, decimal_places=2)
    resident = models.OneToOneField(Resident, verbose_name=_('Resident'), on_delete=models.PROTECT, related_name='room', null=True, blank=True)

    def __str__(self):
        return self.room_code + (f' ({self.resident})' if self.resident else '')

    class Meta:
        verbose_name = _('Room')
        verbose_name_plural = _('Rooms')
