# Generated by Django 4.0.2 on 2022-03-28 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mantenimiento', '0006_alter_empleado_cedula'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cargo',
            name='descripcion',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='departamento',
            name='descripcion',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='cedula',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='nombre',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
