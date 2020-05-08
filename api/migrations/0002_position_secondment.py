# Generated by Django 3.0.2 on 2020-05-06 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='secondment',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='positions', to='api.Secondment'),
            preserve_default=False,
        ),
    ]