# Generated by Django 3.0 on 2019-12-04 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20191204_1706'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supplier',
            old_name='supllierCode',
            new_name='supplierCode',
        ),
    ]
