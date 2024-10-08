# Generated by Django 5.1 on 2024-09-02 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_sales'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-created_at'], 'verbose_name': 'محصول', 'verbose_name_plural': 'محصولات'},
        ),
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد محصول'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sales',
            field=models.IntegerField(default=0, verbose_name='تعداد فروش'),
        ),
    ]
