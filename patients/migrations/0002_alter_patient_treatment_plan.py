# Generated by Django 5.0.1 on 2024-01-15 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='treatment_plan',
            field=models.CharField(max_length=300),
        ),
    ]
