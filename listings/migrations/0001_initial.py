# Generated by Django 5.0.2 on 2024-02-26 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('price', models.FloatField()),
                ('num_beds', models.IntegerField()),
                ('num_bathrooms', models.IntegerField()),
                ('sq_ft', models.IntegerField()),
                ('address', models.CharField(max_length=150)),
                ('description', models.TextField()),
            ],
        ),
    ]