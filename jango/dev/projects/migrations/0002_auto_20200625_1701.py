# Generated by Django 3.0.7 on 2020-06-25 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projects',
            options={'verbose_name': '项目表'},
        ),
        migrations.AlterModelTable(
            name='projects',
            table='tb_table',
        ),
    ]