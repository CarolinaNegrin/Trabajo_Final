# Generated by Django 4.2.3 on 2023-08-06 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='venta',
            old_name='cliente',
            new_name='cliente_id',
        ),
        migrations.RenameField(
            model_name='venta',
            old_name='producto',
            new_name='producto_id',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='subtotal',
        ),
    ]
