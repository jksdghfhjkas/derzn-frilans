# Generated by Django 4.1.1 on 2023-04-05 18:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('drevo', '0062_alter_relationshiptztr_base_tz_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='relation',
            name='director',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rel_director', to=settings.AUTH_USER_MODEL, verbose_name='Руководитель'),
        ),
        migrations.AddField(
            model_name='relation',
            name='expert',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rel_expert', to=settings.AUTH_USER_MODEL, verbose_name='Эксперт'),
        ),
        migrations.CreateModel(
            name='RelationStatuses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('WORK_PRE', 'ПредСвязь в работе'), ('WORK', 'Связь в работе'), ('PRE_FIN', 'Готовая ПредСвязь'), ('FIN', 'Готовая Связь'), ('PRE_EXP', 'Экспертизв ПредСвязи'), ('REJ', 'Отклоненная Связь'), ('PRE_REJ', 'Отклоненная ПредСвязь'), ('PUB_PRE', 'Опубликованная ПредСвязь'), ('PUB', 'Опубликованная Связь')], default=None, max_length=12, null=True, verbose_name='Статус')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('time_limit', models.IntegerField(default=1000, verbose_name='Лимит времени')),
                ('is_active', models.BooleanField(default=True, verbose_name='Текущий статус')),
                ('relation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relation_status', to='drevo.relation', verbose_name='Связь')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_rel_status', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Статус связи',
                'verbose_name_plural': 'Статусы связей',
                'ordering': ['status'],
            },
        ),
    ]
