# Generated by Django 5.1.3 on 2024-12-27 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointment_type',
            field=models.CharField(choices=[('Completed', 'Completed'), ('Running', 'Running'), ('Pending', 'Pending')], default='Pending', max_length=10),
        ),
    ]
