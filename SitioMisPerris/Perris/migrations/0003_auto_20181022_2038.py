# Generated by Django 2.1.2 on 2018-10-22 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Perris', '0002_auto_20181022_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='id_mascota',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]