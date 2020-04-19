# Generated by Django 3.0.5 on 2020-04-19 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='division',
            fields=[
                ('id_div', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='grupo',
            fields=[
                ('id_grp', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='personas',
            name='division',
        ),
        migrations.RemoveField(
            model_name='personas',
            name='id',
        ),
        migrations.RemoveField(
            model_name='personas',
            name='numero_grp',
        ),
        migrations.AddField(
            model_name='personas',
            name='id_personas',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
