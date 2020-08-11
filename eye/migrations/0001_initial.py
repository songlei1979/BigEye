# Generated by Django 3.0.8 on 2020-08-11 06:42

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Allocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AllocationDate', models.DateField()),
            ],
            options={
                'db_table': 'eye_allocation',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hours', models.IntegerField(validators=[django.core.validators.MaxValueValidator(400), django.core.validators.MinValueValidator(1)])),
            ],
            options={
                'db_table': 'eye_assignment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('CaseID', models.AutoField(primary_key=True, serialize=False)),
                ('Description', models.CharField(max_length=40)),
                ('CaseType', models.CharField(choices=[('Insurance Check', 'Insurance Check'), ('Surveillance', 'Surveillance'), ('Credit Check', 'Credit Check'), ('Employee Background Check', 'Employee Background Check'), ('Accident Report', 'Accident Report'), ('Security Inspection', 'Security Inspection')], max_length=50)),
                ('CaseDate', models.DateField()),
                ('Status', models.CharField(choices=[('Open', 'Open'), ('Complete', 'Complete'), ('Closed', 'Closed')], max_length=50)),
                ('Fee', models.FloatField(validators=[django.core.validators.MaxValueValidator(50000), django.core.validators.MinValueValidator(200)])),
                ('Notes', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('ClientID', models.AutoField(primary_key=True, serialize=False)),
                ('LastName', models.CharField(max_length=25)),
                ('FirstName', models.CharField(max_length=25)),
                ('StreetAddress', models.CharField(max_length=50)),
                ('Suburb', models.CharField(max_length=20)),
                ('City', models.CharField(max_length=25)),
                ('PhoneNumbrer', models.CharField(blank=True, max_length=16, null=True)),
                ('EmailAddress', models.CharField(blank=True, max_length=30, null=True)),
                ('ClientStatus', models.CharField(choices=[('Valid', 'Valid'), ('Invalid', 'Invalid')], max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('EquipmentID', models.AutoField(primary_key=True, serialize=False)),
                ('Description', models.CharField(max_length=50)),
                ('Cost', models.FloatField(validators=[django.core.validators.MaxValueValidator(5000), django.core.validators.MinValueValidator(10)])),
            ],
        ),
        migrations.CreateModel(
            name='Investigator',
            fields=[
                ('InvestigatorID', models.AutoField(primary_key=True, serialize=False)),
                ('LastName', models.CharField(max_length=30)),
                ('FirstName', models.CharField(max_length=30)),
                ('StreetAddress', models.CharField(max_length=50)),
                ('Suburb', models.CharField(max_length=20)),
                ('PhoneNumbrer', models.CharField(max_length=16)),
                ('HourlyRate', models.FloatField(validators=[django.core.validators.MaxValueValidator(80), django.core.validators.MinValueValidator(15)])),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('PaymentID', models.AutoField(primary_key=True, serialize=False)),
                ('PaymentDate', models.DateField()),
                ('Amount', models.FloatField(validators=[django.core.validators.MaxValueValidator(50000), django.core.validators.MinValueValidator(50)])),
                ('Case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eye.Case')),
            ],
        ),
        migrations.AddField(
            model_name='case',
            name='Client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eye.Client'),
        ),
    ]
