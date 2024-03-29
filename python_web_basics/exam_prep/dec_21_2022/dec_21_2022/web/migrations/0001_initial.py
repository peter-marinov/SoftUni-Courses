# Generated by Django 4.2.2 on 2023-06-14 05:45

import dec_21_2022.web.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(2)])),
                ('first_name', models.CharField(max_length=20, validators=[dec_21_2022.web.models.check_if_first_letter_is_upper], verbose_name='First name')),
                ('last_name', models.CharField(max_length=20, validators=[dec_21_2022.web.models.check_if_first_letter_is_upper])),
                ('profile_picture', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
