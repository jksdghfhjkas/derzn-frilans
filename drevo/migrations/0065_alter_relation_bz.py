# Generated by Django 3.2.4 on 2023-04-23 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drevo', '0064_auto_20230423_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relation',
            name='bz',
            field=models.ForeignKey(help_text='укажите базовое знание', on_delete=django.db.models.deletion.CASCADE, related_name='base', to='drevo.znanie', verbose_name='Базовое знание'),
        ),
    ]