# Generated by Django 2.1.2 on 2018-11-01 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Perris', '0005_auto_20181101_0124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='foto',
            field=models.ImageField(blank=True, upload_to='static'),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='id_mascota',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
