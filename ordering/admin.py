from django.contrib import admin

# Register your models here.
from ordering.models import Bestellung
from ordering.models import Bestellposition
from ordering.models import Speisekarte

admin.site.register(Bestellung)
admin.site.register(Bestellposition)
admin.site.register(Speisekarte)