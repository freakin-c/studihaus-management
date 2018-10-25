from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext as _

from .models import Resident

from datetime import timedelta, date

def index(request):
    return HttpResponse(_('Hello, Goebenstift!'))

def residents(request):
    residents = Resident.objects.filter(date_move_out=None)
    return render(request, 'residents.html', {'residents': residents})
