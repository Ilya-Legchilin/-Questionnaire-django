# Generated by Django 3.1.7 on 2021-03-06 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quest', '0014_record_number_of_questions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='number_of_questions',
        ),
        migrations.AddField(
            model_name='record',
            name='questionnaire',
            field=models.CharField(default=None, max_length=250, verbose_name='Опрос'),
        ),
    ]
