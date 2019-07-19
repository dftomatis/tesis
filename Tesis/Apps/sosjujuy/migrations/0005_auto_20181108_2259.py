# Generated by Django 2.1.1 on 2018-11-09 01:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sosjujuy', '0004_auto_20181016_1327'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActividadExtension',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=60)),
                ('descripcion', models.CharField(max_length=300)),
                ('fecha', models.DateTimeField()),
                ('presupuesto', models.IntegerField()),
                ('capacidad', models.IntegerField()),
                ('disertante', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sosjujuy.Prestador')),
            ],
        ),
        migrations.RemoveField(
            model_name='actividad_de_extension',
            name='dias_disponibles',
        ),
        migrations.RemoveField(
            model_name='actividad_de_extension',
            name='encargado',
        ),
        migrations.DeleteModel(
            name='Actividad_de_extension',
        ),
    ]