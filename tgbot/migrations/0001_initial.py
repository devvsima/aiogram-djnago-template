# Generated by Django 5.1.6 on 2025-02-07 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TgUsers',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('language', models.CharField(max_length=50)),
                ('username', models.CharField(blank=True, max_length=150, null=True)),
                ('referral', models.IntegerField(default=0)),
                ('is_banned', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'TgUser',
                'verbose_name_plural': 'TgUsers',
                'db_table': 'tgusers',
            },
        ),
    ]
