# Generated by Django 3.1.7 on 2021-03-06 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quest', '0010_auto_20210306_1945'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='dic',
            field=models.CharField(default=None, max_length=250),
        ),
        migrations.AddField(
            model_name='record',
            name='number_of_questions',
            field=models.CharField(default=None, max_length=250),
        ),
        migrations.AddField(
            model_name='record',
            name='questionnaire',
            field=models.CharField(default=None, max_length=250),
        ),
        migrations.AddField(
            model_name='record',
            name='user_id',
            field=models.CharField(default=None, max_length=250),
        ),
    ]
