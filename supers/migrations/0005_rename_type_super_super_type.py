# Generated by Django 4.1.3 on 2022-11-15 22:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supers', '0004_rename_super_type_super_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='super',
            old_name='type',
            new_name='super_type',
        ),
    ]
