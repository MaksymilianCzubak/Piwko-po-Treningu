# Generated by Django 3.0.2 on 2020-01-22 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PortalTreningowy', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainingsession',
            name='level',
        ),
        migrations.AddField(
            model_name='trainingsession',
            name='level',
            field=models.ManyToManyField(to='PortalTreningowy.Plan'),
        ),
    ]
