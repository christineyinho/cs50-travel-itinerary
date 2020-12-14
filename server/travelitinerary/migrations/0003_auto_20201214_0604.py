# Generated by Django 3.1.3 on 2020-12-14 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travelitinerary', '0002_itinerary_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itinerary',
            name='owner',
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='itinerary',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wishlist_itinerary', to='travelitinerary.itinerary'),
        ),
    ]
