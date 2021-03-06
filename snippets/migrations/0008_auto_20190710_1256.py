# Generated by Django 2.2.1 on 2019-07-10 12:56

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0007_auto_20190710_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='perm_list',
            field=models.CharField(default='1,2', max_length=20, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')]),
        ),
    ]
