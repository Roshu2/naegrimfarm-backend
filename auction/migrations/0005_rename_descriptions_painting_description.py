# Generated by Django 4.0.5 on 2022-06-29 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0004_painting_is_auction_alter_painting_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='painting',
            old_name='descriptions',
            new_name='description',
        ),
    ]
