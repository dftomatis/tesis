# Generated by Django 2.1.1 on 2018-11-13 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sosjujuy', '0009_auto_20181113_0040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividadextension',
            name='capacidad',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='actividadextension',
            name='presupuesto',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='beneficiario',
            name='telefono',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='derivacion',
            name='beneficiario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sosjujuy.Beneficiario'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='domicilio',
            name='barrio',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='domicilio',
            name='numero',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='domicilio',
            name='observaciones',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='prestacion',
            name='porcentaje_de_cobertura',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='prestador',
            name='telefono',
            field=models.CharField(max_length=16, null=True),
        ),
    ]