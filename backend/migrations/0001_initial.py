# Generated by Django 4.1.3 on 2022-11-11 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kostyum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('narxi', models.IntegerField(default=24)),
                ('sifati', models.CharField(max_length=24)),
                ('davlati', models.CharField(max_length=24)),
            ],
        ),
    ]
