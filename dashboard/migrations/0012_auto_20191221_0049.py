# Generated by Django 2.2.2 on 2019-12-20 22:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_auto_20191221_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='umuryango',
            name='kpi',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='kpi_name', to='dashboard.KPI'),
        ),
    ]
