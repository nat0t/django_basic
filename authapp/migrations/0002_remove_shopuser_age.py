# Generated by Django 2.2.18 on 2021-03-03 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopuser',
            name='age',
        ),
    ]