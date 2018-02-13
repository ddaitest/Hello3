# Generated by Django 2.0.2 on 2018-02-11 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('reg_date', models.DateTimeField(verbose_name='register at')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.CharField(max_length=200)),
                ('end', models.CharField(max_length=200)),
                ('quota', models.IntegerField(default=1)),
                ('remarks', models.CharField(max_length=200)),
                ('departure', models.DateTimeField(verbose_name='departure')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hope.Driver')),
            ],
        ),
    ]