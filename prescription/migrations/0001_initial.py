# Generated by Django 2.2.1 on 2019-07-04 15:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prescription_date', models.DateField(default=django.utils.timezone.now)),
                ('patient_name', models.CharField(max_length=50)),
                ('patient_age', models.PositiveIntegerField()),
                ('patient_gender', models.CharField(choices=[('Male', 'MALE'), ('Female', 'FEMALE'), ('Other', 'OTHER')], default='OTHER', max_length=10)),
                ('diagnosis', models.CharField(max_length=100000)),
                ('medicines', models.CharField(max_length=100000)),
                ('next_visit_date', models.DateTimeField(blank=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]