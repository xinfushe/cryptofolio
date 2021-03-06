# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(BalanceTimeSeries)
admin.site.register(Currency)
admin.site.register(Exchange)
admin.site.register(ExchangeAccount)
admin.site.register(ExchangeBalance)
admin.site.register(Fiat)
admin.site.register(ManualInput)
admin.site.register(TimeSeries)
admin.site.register(UserProfile)
admin.site.register(Rates)
