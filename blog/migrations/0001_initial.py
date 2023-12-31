# Generated by Django 3.2.8 on 2021-10-08 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('description', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('owner', models.CharField(blank=True, max_length=30, null=True)),
                ('address', models.TextField()),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('property_type', models.CharField(blank=True, choices=[('Apartment', 'Apartment'), ('Bunglow', 'Bunglow'), ('Office', 'Office'), ('Shop', 'Shop')], max_length=30, null=True)),
                ('want_to', models.CharField(blank=True, choices=[('Lease', 'Lease'), ('Rent', 'Rent'), ('Sell', 'Sell')], max_length=30, null=True)),
                ('email_address', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
    ]
