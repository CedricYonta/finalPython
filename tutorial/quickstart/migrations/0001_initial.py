# Generated by Django 4.1.4 on 2022-12-12 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Capteur',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('keyname', models.CharField(max_length=100)),
                ('value', models.CharField(max_length=10)),
            ],
        ),
    ]
