# Generated by Django 4.0.2 on 2022-03-28 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mantenimiento', '0009_alter_cargo_descripcion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='sueldo',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
    ]