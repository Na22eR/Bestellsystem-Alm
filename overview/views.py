import collections
from pprint import pprint

from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import render

from ordering.models import Bestellung, Speisekarte, Bestellposition


@login_required(login_url='home')
def overview(request):
    # quellen: https://stackoverflow.com/questions/43772163/how-to-join-3-tables-in-query-with-django
    # quelle: https://docs.djangoproject.com/en/4.0/topics/db/queries/
    pos_query = Bestellposition.objects.all().order_by('-id').select_related('id_bestellung').select_related('speise')

    '''
    quelle https://docs.python.org/3/library/collections.html#collections.defaultdict
    Generiert ein Object vom Typ defaultdict und gruppiert das Query nach id_bestellung
    '''
    queryset = collections.defaultdict(list)
    for item in pos_query:
        queryset[item.id_bestellung].append(item)

    context = {
        "queryset": dict(queryset)
    }

    return render(request, 'overview.html', context)


# @login_required(login_url='home')
'''def drucken(request):
    return render(request, 'rechnung.html')'''


@login_required(login_url='home')
def bill(request):

    for key in request.GET:
        pos_query = Bestellposition.objects.filter(id_bestellung=key).select_related(
            'id_bestellung').select_related('speise')

        queryset = collections.defaultdict(list)
        for item in pos_query:
            queryset[item.id_bestellung].append(item)

        context = {
            "queryset": dict(queryset)
        }

    return render(request, 'bill.html', context)
