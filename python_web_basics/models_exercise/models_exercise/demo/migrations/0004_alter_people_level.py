# Generated by Django 4.2.1 on 2023-06-01 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0003_people_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='level',
            field=models.CharField(choices=[('Baby', 'Baby'), ('Teen', 'Teen'), ('Old', 'Old')], default='Old', max_length=10),
        ),
    ]
