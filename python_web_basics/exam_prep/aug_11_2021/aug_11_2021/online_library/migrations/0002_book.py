# Generated by Django 4.2.2 on 2023-06-16 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('image_url', models.URLField()),
                ('type', models.CharField(max_length=30)),
            ],
        ),
    ]
