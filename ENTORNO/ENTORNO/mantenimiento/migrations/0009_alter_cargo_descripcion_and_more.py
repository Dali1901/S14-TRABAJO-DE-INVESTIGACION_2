# Generated by Django 4.0.2 on 2022-03-28 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mantenimiento', '0008_alter_empleado_cedula_alter_empleado_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cargo',
            name='descripcion',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='departamento',
            name='descripcion',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
