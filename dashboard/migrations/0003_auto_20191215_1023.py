# Generated by Django 2.2.2 on 2019-12-15 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20191215_0145'),
    ]

    operations = [
        migrations.AddField(
            model_name='umuryango',
            name='kpi',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='dashboard.KPI'),
        ),
        migrations.AlterField(
            model_name='umuryango',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
