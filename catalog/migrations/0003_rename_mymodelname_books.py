# Generated by Django 4.1.3 on 2022-11-29 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_remove_mymodelname_id_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MyModelName',
            new_name='Books',
        ),
    ]