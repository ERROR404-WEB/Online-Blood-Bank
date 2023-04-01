# Generated by Django 4.1 on 2022-10-12 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patient', '0001_initial'),
        ('donor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bloodgroup', models.CharField(max_length=10)),
                ('unit', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='BloodRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=30)),
                ('patient_age', models.PositiveIntegerField()),
                ('reason', models.CharField(max_length=500)),
                ('bloodgroup', models.CharField(max_length=10)),
                ('unit', models.PositiveIntegerField(default=0)),
                ('status', models.CharField(default='Pending', max_length=20)),
                ('date', models.DateField(auto_now=True)),
                ('request_by_donor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='donor.donor')),
                ('request_by_patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='patient.patient')),
            ],
        ),
    ]
