from django.contrib import admin

# Register your models here.
from order.models import Bestellung
from order.models import Bestellposition
from order.models import Speisekarte

admin.site.register(Bestellung)
admin.site.register(Bestellposition)
admin.site.register(Speisekarte)