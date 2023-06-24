# Generated by Django 4.2.2 on 2023-06-24 06:38

import django.core.validators
from django.db import migrations, models
import fruitipedia.web.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25, validators=[django.core.validators.MinLengthValidator(2), fruitipedia.web.validators.check_if_string_starts_with_letter])),
                ('last_name', models.CharField(max_length=35, validators=[django.core.validators.MinLengthValidator(1), fruitipedia.web.validators.check_if_string_starts_with_letter])),
                ('email', models.EmailField(max_length=40)),
                ('password', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(8)])),
                ('image_url', models.URLField(blank=True, null=True, verbose_name='Image URL')),
                ('age', models.IntegerField(blank=True, default=18, null=True)),
            ],
        ),
    ]
