# Generated by Django 3.0.5 on 2020-04-20 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0007_auto_20200420_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='personas',
            name='apellido',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='personas',
            name='nombre',
            field=models.CharField(max_length=20),
        ),
    ]
