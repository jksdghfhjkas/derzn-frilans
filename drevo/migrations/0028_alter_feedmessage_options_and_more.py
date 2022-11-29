# Generated by Django 4.1.1 on 2022-11-08 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drevo', '0027_merge_20221108_1536'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feedmessage',
            options={'verbose_name': 'Сообщение ленты', 'verbose_name_plural': 'Сообщения ленты'},
        ),
        migrations.AlterModelOptions(
            name='labelfeedmessage',
            options={'verbose_name': 'Ярлык сообщений ленты', 'verbose_name_plural': 'Ярлыки сообщений ленты'},
        ),
        migrations.AddField(
            model_name='glossaryterm',
            name='order',
            field=models.PositiveIntegerField(blank=True, help_text='Укажите порядковый номер', null=True, verbose_name='Порядок'),
        ),
    ]