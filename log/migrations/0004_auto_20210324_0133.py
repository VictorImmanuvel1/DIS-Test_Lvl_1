# Generated by Django 2.1.7 on 2021-03-23 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0003_auto_20210324_0129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mark',
            name='mid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='log.User'),
        ),
    ]
