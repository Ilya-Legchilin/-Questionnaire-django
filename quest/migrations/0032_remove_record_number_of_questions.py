# Generated by Django 3.1.7 on 2021-03-06 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quest', '0031_auto_20210306_2005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='number_of_questions',
        ),
    ]
