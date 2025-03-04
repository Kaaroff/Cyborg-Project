from django.db import models
from django.db.models import ForeignKey
from django.core.validators import MaxValueValidator, MinValueValidator

class Category(models.Model):
    title = models.CharField(
        max_length=123,
        verbose_name='Название'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        # verbose_name_plural = 'Категории'

class Image(models.Model):
    file = models.ImageField(
        upload_to='media/product_file',
        verbose_name='Файл'
    )

    class Meta:
        verbose_name = 'Изображение продукта'
        # verbose_name_plural = 'Изображения продуктов'

    def __str__(self):
        return str(self.file)


# TODO: Connect to a user table
class Product(models.Model):
    #user = ForeignKey()
    title = models.CharField(
        max_length=123,
        verbose_name='Название',
        # verbose_name_plural = 'Названия'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        verbose_name = 'Категория'
    )
    images = models.ManyToManyField(
        Image,
        verbose_name='Изображения'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name='Цена'
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Активный'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        # verbose_name_plural = 'Продукты'

# TODO: Connect to a user table
class Rating(models.Model):
    #user = ForeignKey()
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='Продукт'
    )
    count = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name='Оценка'
    )
    comment = models.TextField(
        max_length=500,
        verbose_name='Комментарий'
    )
    # answer = models.TextField(
    #     max_length=500,
    #     verbose_name='Ответ на комментарий',
    #     blank=True,
    #     null=True
    # )
    created_date = models.DateTimeField(
        verbose_name='Дата создания'
    )

    class Meta:
        verbose_name = 'Отзыв',
        # verbose_name_plural = 'Отзывы'

# TODO: Connect to a user table
class RatingAnswer(models.Model):
    # user = ForeignKey()
    rating = models.ForeignKey(
        Rating,
        on_delete=models.CASCADE,
        verbose_name='Отзыв'
    )
    comment = models.TextField(
        max_length=500,
        verbose_name='Комментарий'
    )
    created_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    updated_date =models.DateTimeField(
        auto_now=True,
        verbose_name='Дата изменения'
    )
    time_limit = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name='Ограничение по времени'
    )
    class Meta:
        verbose_name = 'Ответ на отзыв',
        # verbose_name_plural = 'Ответы на отзывы'

# class Order(models.Model):
