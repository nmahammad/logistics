# Generated by Django 5.0.1 on 2024-01-07 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='sender_id',
        ),
        migrations.AlterField(
            model_name='order',
            name='receiver_id',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
