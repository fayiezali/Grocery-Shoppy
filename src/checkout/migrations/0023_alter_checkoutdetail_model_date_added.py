# Generated by Django 4.2.2 on 2023-08-25 16:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0022_alter_checkoutdetail_model_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkoutdetail_model',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 25, 16, 38, 53, 616501, tzinfo=datetime.timezone.utc)),
        ),
    ]
