# Generated by Django 5.0.6 on 2024-07-13 22:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viajes', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='alojamientos',
            options={'ordering': ['-categoriaEstrellas'], 'verbose_name': 'Alojamiento', 'verbose_name_plural': 'Alojamientos'},
        ),
        migrations.AlterModelOptions(
            name='paquetes',
            options={'verbose_name': 'Paquete', 'verbose_name_plural': 'Paquetes'},
        ),
        migrations.AlterModelOptions(
            name='vuelos',
            options={'verbose_name': 'Vuelo', 'verbose_name_plural': 'Vuelos'},
        ),
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='avatares')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
