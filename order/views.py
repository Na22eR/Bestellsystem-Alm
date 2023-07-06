import collections

from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from order.models import Speisekarte
from order.models import Bestellung
from order.models import Bestellposition

Speisekarte_id_name = Speisekarte.objects.values_list('id_name')
list_speisen = []
for sp in Speisekarte_id_name:
    list_speisen.append(sp[0])


def get_gesamtpreis(req_dict):
    gesamtpreis = 0.00
    for x in req_dict:
        if x in list_speisen and int(req_dict[x]) > 0:
            speise = Speisekarte.objects.get(id_name=x)
            preis = speise.preis * int(req_dict[x])
            gesamtpreis += preis
    return gesamtpreis


# https://docs.djangoproject.com/en/4.0/topics/auth/default/
@login_required(login_url='home')
def order(request):
    if request.method == 'GET':
        # Bestellseite für neue Bestellungen zurück gegeben
        speisen = Speisekarte.objects.all()
        context = {
            "speisen": speisen,
        }
        return render(request, 'order/new_order.html', context)

    if request.method == 'POST':

        # Eintrag für Tabelle Bestellung
        tisch_nr = request.POST['tisch_nr']
        uhrzeit = datetime.now().strftime("%d.%m.%Y/%H-%M-%S")
        bedienung = request.user  # request.user.id
        gesamtpreis = get_gesamtpreis(request.POST)
        new_best = Bestellung(tisch_nr=tisch_nr, uhrzeit=uhrzeit, bedienung=bedienung, gesamtpreis=gesamtpreis)
        new_best.save()

        # Eintrag für Tabelle Bestellposition
        for x in request.POST:
            if x in list_speisen and int(request.POST[x]) > 0:
                id_bestellung = Bestellung.objects.get(pk=new_best.id)
                speise = Speisekarte.objects.get(id_name=x)
                anzahl = request.POST[x]
                anmerkung = request.POST['amk_' + x]
                preis = speise.preis
                b_pos = Bestellposition(id_bestellung=id_bestellung, speise=speise, anzahl=anzahl, anmerkung=anmerkung,
                                        preis=preis)
                b_pos.save()

        # Eintrag für Tabelle Speisekarte
        for x in request.POST:
            if x in list_speisen and int(request.POST[x]) > 0:
                speise = Speisekarte.objects.get(id_name=x)
                anzahl_table = int(speise.anzahl_bestellt)
                anzahl_best = int(request.POST[x])
                anzahl_new = anzahl_table + anzahl_best
                speise.anzahl_bestellt = anzahl_new
                speise.save()

        pos_query = Bestellposition.objects.filter(id_bestellung=id_bestellung).select_related(
            'id_bestellung').select_related('speise')

        print(pos_query)

        queryset = collections.defaultdict(list)
        for item in pos_query:
            queryset[item.id_bestellung].append(item)

        context = {
            "queryset": dict(queryset)
        }

        return render(request, 'overview/bill.html', context)