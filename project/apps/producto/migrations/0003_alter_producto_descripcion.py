# Generated by Django 4.2.3 on 2023-08-06 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0002_rename_categoria_producto_categoria_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
