# Generated by Django 3.0.2 on 2020-05-11 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20200511_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluation',
            name='status',
            field=models.CharField(choices=[('created', 'created'), ('ise_auth_pending', 'ise_auth_pending'), ('int_auth_pending', 'int_auth_pending'), ('schedule_pending', 'schedule_pending'), ('schedule_pending', 'schedule_pending'), ('dont_eval', 'dont_eval'), ('not_evaluable', 'not_evaluable')], default='created', max_length=255),
        ),
    ]
