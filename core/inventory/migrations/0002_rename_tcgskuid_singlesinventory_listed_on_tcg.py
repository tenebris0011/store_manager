# Generated by Django 4.0.6 on 2022-08-08 20:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='singlesinventory',
            old_name='tcgSkuId',
            new_name='listed_on_tcg',
        ),
    ]
