# Generated by Django 4.2.17 on 2024-12-22 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0002_alter_buyer_balance_alter_game_age_limited_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
            ],
        ),
    ]
