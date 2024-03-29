# Generated by Django 4.2.1 on 2023-06-02 12:57

from django.db import migrations, models
import models_demos.web.validators


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0030_alter_department_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='age',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='employee',
            name='start_date',
            field=models.DateField(validators=[models_demos.web.validators.validate_in_the_past]),
        ),
    ]
