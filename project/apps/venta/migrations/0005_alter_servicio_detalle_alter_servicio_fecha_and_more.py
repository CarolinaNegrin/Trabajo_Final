# Generated by Django 4.2.3 on 2023-08-08 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0004_servicio_color_servicio_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='detalle',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='fecha',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='fecha_servicio',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='tiposervicio',
            name='nombre',
            field=models.CharField(max_length=150),
        ),
    ]
