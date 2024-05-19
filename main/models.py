from django.db import models
from django.utils import timezone

NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    """
    Модель Category
    :param:
    - Имя name
    - Описание description
    """
    name = models.CharField(max_length=250, verbose_name='Название', help_text="Введите название категории",)
    description = models.TextField(verbose_name='Описание', **NULLABLE, help_text="Введите описание категории",)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    """
    Модель Product
    :param:
    - Имя name
    - Описание description
    - Изображение (превью) preview
    - Категория category
    - Цена за покупку price
    - Дата создания (записи в БД) created_at
    - Дата последнего изменения (записи в БД) updated_at
    """
    name = models.CharField(max_length=250, verbose_name='Наименование', help_text="Введите наименование",)
    description = models.TextField(verbose_name='Описание', **NULLABLE, help_text="Введите описание",)
    preview = models.ImageField(upload_to='product/photo', **NULLABLE, verbose_name='Превью', help_text="Загрузите изображение",)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория', help_text="Введите категорию", related_name="categories",)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена', help_text="Введите цену",)
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Дата создания', help_text="Введите дату создания",)
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата последнего изменения', help_text="Введите дату изменения",)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ["category", "name"]


class Contact(models.Model):
    """
    Модель Contact
    :param:
    - Имя name
    - Телефон phone:
    - Сообщение message
    - Дата отправки created_at
    """
    name = models.CharField(max_length=50, verbose_name="Имя", help_text="Введите имя", )
    phone = models.CharField(max_length=20, verbose_name="Телефон", help_text="Введите телефон", )
    message = models.TextField(verbose_name="Сообщение", help_text="Введите сообщение", **NULLABLE)
    created_at = models.DateTimeField(default=timezone.now, **NULLABLE, verbose_name="Дата создания", help_text="Введите дату создания", )

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return f"{self.name} - {self.phone}"
