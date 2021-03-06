# Generated by Django 3.0.2 on 2020-01-21 21:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=64)),
                ('goal', models.TextField()),
                ('description', models.TextField()),
                ('hours_per_week', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TrainingSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)])),
                ('day', models.IntegerField(choices=[(1, 'Monday'), (2, 'Teusday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')])),
                ('details', models.TextField()),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='PortalTreningowy.Plan')),
            ],
        ),
    ]
