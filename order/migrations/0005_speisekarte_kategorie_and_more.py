# Generated by Django 4.0.5 on 2023-07-06 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_alter_speisekarte_anzahl_bestellt'),
    ]

    operations = [
        migrations.AddField(
            model_name='speisekarte',
            name='kategorie',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bestellposition',
            name='anmerkung',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='bestellung',
            name='uhrzeit',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
