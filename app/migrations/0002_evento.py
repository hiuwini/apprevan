# Generated by Django 2.0.13 on 2019-11-12 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('e_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('lugar', models.CharField(max_length=200)),
                ('fecha', models.CharField(max_length=20)),
            ],
        ),
    ]
