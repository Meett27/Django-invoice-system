# Generated by Django 2.2.8 on 2020-07-15 12:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_no', models.IntegerField()),
                ('invoice_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('vendor_name', models.CharField(max_length=100)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='collections', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CollectionTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_description', models.CharField(max_length=256)),
                ('item_quantity', models.PositiveIntegerField()),
                ('item_rate', models.PositiveIntegerField()),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoice', to='mycollections.Collection')),
            ],
        ),
    ]
