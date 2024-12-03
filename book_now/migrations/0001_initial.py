# Generated by Django 4.2.16 on 2024-12-03 20:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('treatments', '0003_auto_20241128_2241'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('booking_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('appointment_date', models.DateField()),
                ('appointment_time', models.TimeField()),
                ('requests', models.CharField(max_length=200)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('treatment_selected', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='treatments.treatment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['appointment_date'],
            },
        ),
    ]
