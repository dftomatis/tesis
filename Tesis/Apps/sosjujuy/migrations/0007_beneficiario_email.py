# Generated by Django 2.1.1 on 2018-11-12 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sosjujuy', '0006_encuestaatencionbeneficiario'),
    ]

    operations = [
        migrations.AddField(
            model_name='beneficiario',
            name='email',
            field=models.EmailField(default='sosjujuy@yopmail.com', max_length=70),
        ),
    ]