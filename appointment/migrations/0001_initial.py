# Generated by Django 5.0.6 on 2024-12-14 12:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profile1', '0001_initial'),
        ('tuition', '0004_alter_availabletime_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_types', models.CharField(choices=[('Offline', 'Offline'), ('Online', 'Online')], max_length=10)),
                ('appointment_status', models.CharField(choices=[('Completed', 'Completed'), ('Pending', 'Pending'), ('Running', 'Running')], default='Pending', max_length=10)),
                ('symtom', models.TextField()),
                ('cancel', models.BooleanField(default=False)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile1.student')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tuition.tuitionteacher')),
                ('time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tuition.availabletime')),
            ],
        ),
    ]
