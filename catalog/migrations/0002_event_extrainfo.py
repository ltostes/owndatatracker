# Generated by Django 3.0.6 on 2020-05-17 02:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100)),
                ('event', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ExtraInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extra_info', models.CharField(max_length=5000)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Event')),
            ],
        ),
    ]
