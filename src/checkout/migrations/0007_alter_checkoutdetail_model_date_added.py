# Generated by Django 4.2.2 on 2023-08-18 21:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_alter_checkoutdetail_model_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkoutdetail_model',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 18, 21, 49, 21, 765548, tzinfo=datetime.timezone.utc)),
        ),
    ]
