# Generated by Django 5.0.6 on 2024-06-11 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0003_alter_task_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='data',
            field=models.JSONField(blank=True, default='{"price":"0"}'),
        ),
    ]
