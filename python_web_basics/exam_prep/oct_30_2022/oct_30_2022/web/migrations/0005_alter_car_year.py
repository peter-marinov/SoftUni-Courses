# Generated by Django 4.2.2 on 2023-06-14 18:55

from django.db import migrations, models
import oct_30_2022.web.models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_car'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.IntegerField(validators=[oct_30_2022.web.models.check_if_year_in_between]),
        ),
    ]
