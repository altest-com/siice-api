# Generated by Django 3.0.2 on 2020-05-09 20:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200506_1412'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='year',
        ),
        migrations.AddField(
            model_name='application',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='evaluation',
            name='mode',
            field=models.CharField(choices=[('ordinary', 'ordinary'), ('extra', 'extra'), ('repeat', 'repeat')], default='ordinary', max_length=255),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='type',
            field=models.CharField(choices=[('entrant', 'entrant'), ('reentrant', 'reentrant'), ('permanence', 'permanence'), ('promotion', 'promotion')], default='entrant', max_length=255),
        ),
    ]
