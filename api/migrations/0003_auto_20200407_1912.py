# Generated by Django 3.0.2 on 2020-04-08 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200407_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medical',
            name='passed',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='polygraphic',
            name='passed',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='psychological',
            name='passed',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='socioeconomic',
            name='passed',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='toxicological',
            name='passed',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
