# Generated by Django 4.0.4 on 2023-06-26 09:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Speisekarte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('preis', models.DecimalField(decimal_places=2, max_digits=7)),
                ('anzahl', models.IntegerField()),
                ('anzahl_bestellt', models.IntegerField()),
                ('limit', models.BooleanField()),
                ('verfuegbar', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Bestellung',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tisch_nr', models.IntegerField()),
                ('uhrzeit', models.DateTimeField()),
                ('gesamtpreis', models.DecimalField(decimal_places=2, max_digits=7)),
                ('bedienung', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bestellposition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anzahl', models.IntegerField()),
                ('anmerkung', models.CharField(max_length=200)),
                ('id_bestellung', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.bestellung')),
                ('speise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.speisekarte')),
            ],
        ),
    ]
