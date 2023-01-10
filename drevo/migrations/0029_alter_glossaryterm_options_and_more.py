# Generated by Django 4.1.1 on 2022-12-17 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drevo', '0028_alter_feedmessage_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='glossaryterm',
            options={'ordering': ('order', 'name'), 'verbose_name': 'Термин глоссария', 'verbose_name_plural': 'Термины глоссария'},
        ),
        migrations.AddField(
            model_name='interviewanswerexpertproposal',
            name='is_notified',
            field=models.BooleanField(default=False, verbose_name='Уведомлён'),
        ),
    ]