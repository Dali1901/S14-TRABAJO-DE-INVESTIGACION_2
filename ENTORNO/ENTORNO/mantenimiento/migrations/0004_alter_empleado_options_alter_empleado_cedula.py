# Generated by Django 4.0.2 on 2022-03-27 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mantenimiento', '0003_empleado_cedula'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='empleado',
            options={'ordering': ['nombre'], 'verbose_name': 'Empleado', 'verbose_name_plural': 'Empleados'},
        ),
        migrations.AlterField(
            model_name='empleado',
            name='cedula',
            field=models.DecimalField(decimal_places=0, max_digits=8),
        ),
    ]
