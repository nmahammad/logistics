# Generated by Django 5.0.1 on 2024-01-07 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0003_order_sender_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(default='pending', max_length=50, null=True),
        ),
    ]