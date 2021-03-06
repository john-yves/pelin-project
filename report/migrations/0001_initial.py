# Generated by Django 2.2.2 on 2019-12-14 23:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_type', models.CharField(max_length=300)),
                ('igihe_itangirwa', models.PositiveSmallIntegerField(choices=[(1, 'Icyumweru'), (2, 'Igihembwe'), (3, 'Umwaka')])),
                ('deadline', models.DateTimeField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Department')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('date', models.DateTimeField()),
                ('report_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.ReportType')),
            ],
        ),
    ]
