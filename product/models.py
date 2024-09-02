from django.contrib.auth.models import User
from django.db import models
from django.utils.html import format_html
from django.utils.text import slugify



class Brand(models.Model):
    name = models.CharField(max_length=50, verbose_name="برند")

    class Meta:
        verbose_name = "برند"
        verbose_name_plural = "برندها"

    def __str__(self):
        return self.name




class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="دسته بندی")

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

    def __str__(self):
        return self.name




class Color(models.Model):
    name = models.CharField(max_length=50, verbose_name="رنگ")

    class Meta:
        verbose_name = "رنگ"
        verbose_name_plural = "رنگ ها"

    def __str__(self):
        return self.name


discount_list = [(0, 'بدون تخفیف'),(1, '1%'), (2, '2%'), (3, '3%'), (4, '4%'), (5, '5%'), (6, '6%'), (7, '7%'), (8, '8%'), (9, '9%'),
                 (10, '10%'), (11, '11%'), (12, '12%'), (13, '13%'), (14, '14%'), (15, '15%'), (16, '16%'), (17, '17%'),
                 (18, '18%'), (19, '19%'), (20, '20%'), (21, '21%'), (22, '22%'), (23, '23%'), (24, '24%'), (25, '25%'),
                 (26, '26%'), (27, '27%'), (28, '28%'), (29, '29%'), (30, '30%'), (31, '31%'), (32, '32%'), (33, '33%'),
                 (34, '34%'), (35, '35%'), (36, '36%'), (37, '37%'), (38, '38%'), (39, '39%'), (40, '40%'), (41, '41%'),
                 (42, '42%'), (43, '43%'), (44, '44%'), (45, '45%'), (46, '46%'), (47, '47%'), (48, '48%'), (49, '49%'),
                 (50, '50%'), (51, '51%'), (52, '52%'), (53, '53%'), (54, '54%'), (55, '55%'), (56, '56%'), (57, '57%'),
                 (58, '58%'), (59,
                               '59%'), (60, '60%'), (61, '61%'), (62, '62%'), (63, '63%'), (64, '64%'), (65, '65%'),
                 (66, '66%'), (67, '67%'), (68, '68%'), (69, '69%'), (70, '70%'), (71, '71%'), (72, '72%'), (73, '73%'),
                 (74, '74%'), (75, '75%'), (76, '76%'), (77, '77%'), (78, '78%'), (79, '79%'), (80, '80%'), (81, '81%'),
                 (82, '82%'), (83, '83%'), (84, '84%'), (85, '85%'), (86, '86%'), (87, '87%'), (88, '88%'), (89, '89%'),
                 (90, '90%'), (91, '91%'),
                 (92, '92%'), (93, '93%'), (94, '94%'), (95, '95%'), (96, '96%'), (97, '97%'), (98, '98%'), (99, '99%'),
                 (100, '100%')]



class Product(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="نام محصول")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="brands", verbose_name="برند")
    category = models.ManyToManyField(Category, related_name="categories", verbose_name="دسته بندی")
    color = models.ManyToManyField(Color, related_name="colors", verbose_name="رنگ")
    marketer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="marketers", verbose_name="فروشنده")
    price = models.IntegerField(verbose_name="قیمت")
    discount = models.IntegerField(verbose_name="تخفیف", choices=discount_list, default=0)
    numbers = models.IntegerField(default=1,verbose_name="تعداد موجودی")
    description = models.TextField(verbose_name="توضیحات")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد محصول")
    sales = models.IntegerField(default=0, verbose_name="تعداد فروش")


    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"
        ordering = ['-created_at']


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)


    def show_image(self):
        if self.image_set.all()[0]:
            return format_html(f'<img src="{self.image_set.all()[0].image.url}" width="50" height="50" />')
        else:
            return format_html("<h4 style='color:red' >تصویر ندارد</h4>")

    show_image.short_description = "عکس"


    def get_total_price(self):
        total_price = self.price-(self.price*self.discount/100)
        return int(total_price)





class ShortInfo(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="محصول")
    title = models.CharField(max_length=50, verbose_name="نام ویژگی")
    value = models.CharField(max_length=50, verbose_name="مقدار ویژگی")

    class Meta:
        verbose_name = "ویژگی"
        verbose_name_plural = "ویژگی ها"

    def __str__(self):
        return self.title





class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="محصول")
    image = models.ImageField(upload_to="product/images", verbose_name="عکس")

    class Meta:
        verbose_name = "عکس"
        verbose_name_plural = "عکس ها"





class GoodOrBadPoint(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="محصول")
    good_or_bad= models.CharField(max_length=50,choices=(("good", "ویژگی مثبت"),("bad", "ویژگی منفی")), default="good", verbose_name="انتخاب کنید")
    name = models.CharField(max_length=50, verbose_name="ویژگی مدنظر")

    class Meta:
        verbose_name = "نقطه قوت یا ضعف"
        verbose_name_plural = "نقاط قوت یا ضعف"

    def __str__(self):
        return self.name