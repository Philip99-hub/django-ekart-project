# Generated by Django 4.2.7 on 2023-12-20 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eKart_admin', '0002_category'),
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_no', models.CharField(max_length=30)),
                ('product_name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
                ('stock', models.IntegerField()),
                ('price', models.FloatField()),
                ('image', models.ImageField(upload_to='product/')),
                ('rating', models.FloatField(default=0)),
                ('status', models.CharField(default='available', max_length=20)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eKart_admin.category')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.seller')),
            ],
            options={
                'db_table': 'product_tb',
            },
        ),
    ]
