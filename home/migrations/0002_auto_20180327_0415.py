# Generated by Django 2.0.1 on 2018-03-27 04:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cug',
            old_name='paln',
            new_name='plan',
        ),
        migrations.AddField(
            model_name='employee',
            name='office_number',
            field=models.CharField(default=0, max_length=10, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='other_phone_no',
            field=models.CharField(default=0, max_length=12, unique=True, validators=[django.core.validators.RegexValidator('^[0-9]{1,12}$', 'Only Numbers and Upper are allowed (max. 6)')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='quarter_number',
            field=models.CharField(default=0, max_length=10, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='residence_number',
            field=models.CharField(default=0, max_length=10, unique=True),
            preserve_default=False,
        ),
    ]
