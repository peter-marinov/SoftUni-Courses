# Generated by Django 4.2.1 on 2023-06-01 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0005_alter_people_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=10, unique=True)),
            ],
        ),
    ]
