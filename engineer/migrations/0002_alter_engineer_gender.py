# Generated by Django 5.0.3 on 2025-04-15 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engineer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='engineer',
            name='gender',
            field=models.CharField(choices=[('M', 'male'), ('F', 'female')], max_length=1),
        ),
    ]
