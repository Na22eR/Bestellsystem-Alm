import collections

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from order.models import Bestellung, Speisekarte, Bestellposition


@login_required(login_url='home')
def overview(request):
    # quelle: https://docs.djangoproject.com/en/4.0/topics/db/queries/
    pos_query = Bestellposition.objects.all().order_by('-id').select_related('id_bestellung').select_related('speise')

    queryset = collections.defaultdict(list)
    for item in pos_query:
        queryset[item.id_bestellung].append(item)

    context = {
        "queryset": dict(queryset)
    }

    return render(request, 'overview/overview.html', context)


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

    return render(request, 'overview/bill.html', context)