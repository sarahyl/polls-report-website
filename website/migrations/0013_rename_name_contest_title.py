# Generated by Django 5.0.1 on 2024-06-12 00:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_contest_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contest',
            old_name='name',
            new_name='title',
        ),
    ]
