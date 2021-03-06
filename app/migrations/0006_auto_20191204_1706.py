# Generated by Django 3.0 on 2019-12-04 11:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0005_delete_userdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('addressname', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('pincode', models.CharField(max_length=6)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aduser', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('OrderNo', models.CharField(max_length=15)),
                ('payment', models.CharField(choices=[('Offline', 'Offline'), ('Online', 'Online')], default='Offline', max_length=10)),
                ('shipaddress', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address', to='app.Address')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orduser', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='product',
            name='gst',
            field=models.CharField(choices=[(5, '5'), (12, '12'), (18, '18'), (28, '28')], default=18, max_length=2),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('ordsale', models.DecimalField(decimal_places=2, max_digits=8)),
                ('ordpurchase', models.DecimalField(decimal_places=2, max_digits=8)),
                ('ordgst', models.CharField(choices=[(5, '5'), (12, '12'), (18, '18'), (28, '28')], default=18, max_length=2)),
                ('orderitemstatus', models.CharField(choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered')], default='Pending', max_length=15)),
                ('orderid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='app.Order')),
                ('productid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='app.Product')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
