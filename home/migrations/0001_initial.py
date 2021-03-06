# Generated by Django 2.0 on 2018-04-04 16:09

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('department_number', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True, validators=[django.core.validators.RegexValidator('^[0-9]{1,6}$', 'Only Numbers and Upper are allowed (max. 6)')])),
                ('department_name', models.CharField(max_length=200, unique=True)),
                ('department_short_name', models.CharField(max_length=100, unique=True)),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='DeptType',
            fields=[
                ('type_number', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('type_name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Designation',
            fields=[
                ('designation_number', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True, validators=[django.core.validators.RegexValidator('^[0-9]{1,6}$', 'Only Numbers and Upper are allowed (max. 6)')])),
                ('designation_name', models.CharField(max_length=200, unique=True)),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True, validators=[django.core.validators.RegexValidator('^[0-9]{1,10}$', 'Only Numbers and Upper are allowed (max. 6)')])),
                ('name', models.CharField(max_length=200)),
                ('personal_phone_no', models.CharField(max_length=12, validators=[django.core.validators.RegexValidator('^[0-9]{1,12}$', 'Only Numbers and Upper are allowed (max. 6)')])),
                ('other_phone_no', models.CharField(max_length=12, validators=[django.core.validators.RegexValidator('^[0-9]{1,12}$', 'Only Numbers and Upper are allowed (max. 6)')])),
                ('email_id', models.EmailField(max_length=254)),
                ('quarter_number', models.CharField(max_length=10)),
                ('residence_number', models.CharField(max_length=10)),
                ('office_number', models.CharField(max_length=10)),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='date published')),
                ('department_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Department')),
                ('designation_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Designation')),
            ],
        ),
        migrations.AddField(
            model_name='department',
            name='department_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.DeptType'),
        ),
    ]
