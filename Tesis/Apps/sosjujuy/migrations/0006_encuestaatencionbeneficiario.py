# Generated by Django 2.1.1 on 2018-11-12 03:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sosjujuy', '0005_auto_20181108_2259'),
    ]

    operations = [
        migrations.CreateModel(
            name='EncuestaAtencionBeneficiario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('atendido', models.BooleanField()),
                ('nivel_de_atencion', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=0)),
                ('nivel_de_puntualidad', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=0)),
                ('observacion', models.CharField(max_length=300)),
                ('beneficiario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sosjujuy.Beneficiario')),
                ('derivacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sosjujuy.Derivacion')),
            ],
        ),
    ]