# Generated by Django 4.2.2 on 2023-08-15 22:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '0003_alter_orderdetailsmodel_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckoutDetail_MODEL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CheckoutDetail_phone_number', models.CharField(blank=True, max_length=10, null=True)),
                ('CheckoutDetail_total_amount', models.CharField(blank=True, max_length=10, null=True)),
                ('CheckoutDetail_address', models.CharField(max_length=300)),
                ('CheckoutDetail_city', models.CharField(max_length=100)),
                ('CheckoutDetail_state', models.CharField(max_length=100)),
                ('CheckoutDetail_zipcode', models.CharField(max_length=100)),
                ('CheckoutDetail_payment', models.CharField(blank=True, max_length=100)),
                ('CheckoutDetail_date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('CheckoutDetail_order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.ordermodel')),
                ('CheckoutDetail_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
