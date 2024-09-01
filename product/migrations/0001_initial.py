# Generated by Django 5.1 on 2024-09-01 20:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='برند')),
            ],
            options={
                'verbose_name': 'برند',
                'verbose_name_plural': 'برندها',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='دسته بندی')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='رنگ')),
            ],
            options={
                'verbose_name': 'رنگ',
                'verbose_name_plural': 'رنگ ها',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='نام محصول')),
                ('price', models.IntegerField(verbose_name='قیمت')),
                ('discount', models.IntegerField(choices=[(0, 'بدون تخفیف'), (1, '1%'), (2, '2%'), (3, '3%'), (4, '4%'), (5, '5%'), (6, '6%'), (7, '7%'), (8, '8%'), (9, '9%'), (10, '10%'), (11, '11%'), (12, '12%'), (13, '13%'), (14, '14%'), (15, '15%'), (16, '16%'), (17, '17%'), (18, '18%'), (19, '19%'), (20, '20%'), (21, '21%'), (22, '22%'), (23, '23%'), (24, '24%'), (25, '25%'), (26, '26%'), (27, '27%'), (28, '28%'), (29, '29%'), (30, '30%'), (31, '31%'), (32, '32%'), (33, '33%'), (34, '34%'), (35, '35%'), (36, '36%'), (37, '37%'), (38, '38%'), (39, '39%'), (40, '40%'), (41, '41%'), (42, '42%'), (43, '43%'), (44, '44%'), (45, '45%'), (46, '46%'), (47, '47%'), (48, '48%'), (49, '49%'), (50, '50%'), (51, '51%'), (52, '52%'), (53, '53%'), (54, '54%'), (55, '55%'), (56, '56%'), (57, '57%'), (58, '58%'), (59, '59%'), (60, '60%'), (61, '61%'), (62, '62%'), (63, '63%'), (64, '64%'), (65, '65%'), (66, '66%'), (67, '67%'), (68, '68%'), (69, '69%'), (70, '70%'), (71, '71%'), (72, '72%'), (73, '73%'), (74, '74%'), (75, '75%'), (76, '76%'), (77, '77%'), (78, '78%'), (79, '79%'), (80, '80%'), (81, '81%'), (82, '82%'), (83, '83%'), (84, '84%'), (85, '85%'), (86, '86%'), (87, '87%'), (88, '88%'), (89, '89%'), (90, '90%'), (91, '91%'), (92, '92%'), (93, '93%'), (94, '94%'), (95, '95%'), (96, '96%'), (97, '97%'), (98, '98%'), (99, '99%'), (100, '100%')], default=0, verbose_name='تخفیف')),
                ('numbers', models.IntegerField(default=1, verbose_name='تعداد موجودی')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('slug', models.SlugField(blank=True, null=True, verbose_name='اسم در دامنه')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brands', to='product.brand', verbose_name='برند')),
                ('category', models.ManyToManyField(related_name='categories', to='product.category', verbose_name='دسته بندی')),
                ('color', models.ManyToManyField(related_name='colors', to='product.color', verbose_name='رنگ')),
                ('marketer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='marketers', to=settings.AUTH_USER_MODEL, verbose_name='فروشنده')),
            ],
            options={
                'verbose_name': 'محصول',
                'verbose_name_plural': 'محصولات',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product/images', verbose_name='عکس')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='محصول')),
            ],
            options={
                'verbose_name': 'عکس',
                'verbose_name_plural': 'عکس ها',
            },
        ),
        migrations.CreateModel(
            name='ShortInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='نام ویژگی')),
                ('value', models.CharField(max_length=50, verbose_name='مقدار ویژگی')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='محصول')),
            ],
            options={
                'verbose_name': 'ویژگی',
                'verbose_name_plural': 'ویژگی ها',
            },
        ),
    ]