# Generated by Django 2.1.2 on 2018-11-01 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Perris', '0006_auto_20181101_0146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='id_mascota',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
