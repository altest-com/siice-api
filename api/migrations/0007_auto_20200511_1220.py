# Generated by Django 3.0.2 on 2020-05-11 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_remove_evaluation_scheduled_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluation',
            name='reason',
            field=models.CharField(choices=[('none', 'none'), ('periodic', 'periodic'), ('tracking', 'tracking')], default='none', max_length=255),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='status',
            field=models.CharField(choices=[('created', 'created'), ('ise_auth_pending', 'ise_auth_pending'), ('int_auth_pending', 'int_auth_pending'), ('schedule_pending', 'schedule_pending'), ('schedule_pending', 'schedule_pending')], default='created', max_length=255),
        ),
    ]
