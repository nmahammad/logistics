# Generated by Django 5.0.1 on 2024-01-07 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0002_remove_order_sender_id_alter_order_receiver_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='sender_id',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
