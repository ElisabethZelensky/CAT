import datetime
import os

from django.conf import settings
from django.db import models
from django.utils import timezone


class Product(models.Model):
    """
    Изделие
    """
    DEFAULT_PK = 1
    name = models.CharField(max_length=100, default='Наименование', verbose_name='Наименование изделия')
    sizes = models.CharField(max_length=100, default='Размеры', verbose_name='Размеры изделия')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'изделие'
        verbose_name_plural = 'Изделия'


class Provider(models.Model):
    """
    Поставщик
    """
    DEFAULT_PK = 1
    name = models.CharField(max_length=100, default='Поставщик', verbose_name='Наименование')
    address = models.CharField(max_length=100, blank=True, null=True, verbose_name='Адрес')
    delivery_period = models.DateField(default=timezone.now, verbose_name='Срок доставки')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'поставщик'
        verbose_name_plural = 'Поставщики'


class Ingredient(models.Model):
    """
    Ингрeдиент
    """
    DEFAULT_PK = 1
    articul = models.CharField(max_length=20, default=0, unique=True, verbose_name='Артикул')
    name = models.CharField(max_length=30, default='Введите наименование ингредиента', verbose_name='Наименование')
    measure_unit = models.CharField(max_length=30, default='Введите единицу измерения', verbose_name='Единицы измерения')
    amount = models.FloatField(default=0, verbose_name='Количество')
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, default=Provider.DEFAULT_PK,
                                 blank=True, null=True, verbose_name='Поставщик')
    expired = models.DateTimeField(default=timezone.now, verbose_name='Срок годности')
    image = models.ImageField(blank=True, null=True, upload_to='pictures/%Y/%m/%d/')
    ingredient_type = models.CharField(max_length=30, default='Введите тип ингредиента', verbose_name='Тип Ингредиента')
    purchase_price = models.FloatField(default=0, verbose_name='Закупочная цена')
    gost = models.CharField(max_length=10, blank=True, null=True, verbose_name='ГОСТ')
    packing = models.CharField(max_length=20, blank=True, null=True, verbose_name='Фасовка')
    characteristic = models.TextField(blank=True, null=True, verbose_name='Характеристика')

    def url(self):
        return os.path.join(settings.STATIC_URL, os.path.basename(str(self.image)))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ингрeдиент'
        verbose_name_plural = 'Ингрeдиенты'


class Decoration(models.Model):
    """
    Украшение для торта
    """
    DEFAULT_PK = 1
    articul = models.CharField(max_length=20, default=0, unique=True, verbose_name='Артикул')
    name = models.CharField(max_length=30, default='Введите наименование украшения', verbose_name='Наименование')
    measure_unit = models.CharField(max_length=30, default='Введите единицу измерения',
                                    verbose_name='Единицы измерения')
    amount = models.FloatField(default=0, verbose_name='Количество')
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, default=Provider.DEFAULT_PK,
                                 blank=True, null=True, verbose_name='Поставщик')
    expired = models.DateTimeField(default=timezone.now, verbose_name='Срок годности')
    image = models.ImageField(blank=True, null=True, verbose_name='Изображение')
    decoration_type = models.CharField(max_length=30, default='Введите тип украшения', verbose_name='Тип украшения')
    purchase_price = models.FloatField(default=0, verbose_name='Закупочная цена')
    weight = models.FloatField(default=0, verbose_name='Вес единицы украшения')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'украшение для торта'
        verbose_name_plural = 'Украшения для торта'


class DecorationSpecification(models.Model):
    """
    Спецификация украшения для торта
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Изделие', default=Product.DEFAULT_PK)
    decoration = models.ForeignKey(Decoration, on_delete=models.CASCADE, verbose_name='Украшение для торта',
                                   null=True, default = None)
    amount = models.FloatField(default=0, verbose_name='Количество', blank=True)

    def __str__(self):
        return '{} {}'.format(self.product, self.decoration)

    class Meta:
        verbose_name = 'спецификация украшения для торта'
        verbose_name_plural = 'Спецификации украшения для торта'


class SemifinishedSpecification(models.Model):
    """
    Спецификация полуфабрикаты
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Изделие', related_name="product",
                                default=Product.DEFAULT_PK)
    semifinished = models.ForeignKey(Product, on_delete=models.CASCADE, default = None, null=True,
                                     verbose_name='Полуфабрикат', related_name="semifinished")
    amount = models.FloatField(default=0, verbose_name='Количество', blank=True)

    def __str__(self):
        return '{} {}'.format(self.product, self.semifinished)

    class Meta:
        verbose_name = 'спецификация полуфабрикаты'
        verbose_name_plural = 'Спецификации полуфабрикаты'


class ProductSpecification(models.Model):
    """
    Спецификация ингрeдиенты
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Изделие', default=Product.DEFAULT_PK)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, verbose_name='Ингредиент', null=True,
                                   default = None)
    amount = models.FloatField(default=0, verbose_name='Количество', blank=True)

    def __str__(self):
        return '{} {}'.format(self.product, self.ingredient)

    class Meta:
        verbose_name = 'спецификация ингредиенты'
        verbose_name_plural = 'Спецификации ингредиенты'


class EquipmentType(models.Model):
    """
    Тип оборудования
    """
    # DEFAULT_PK = 1
    #
    # TYPE1 = 'Тип 1'
    # TYPE2 = 'Тип 2'
    # TYPE3 = 'Тип 3'
    #
    # TYPES = [
    #     (TYPE1, 'Тип 1'),
    #     (TYPE2, 'Тип 2'),
    #     (TYPE3, 'Тип 3'),
    # ]
    equipment_type = models.CharField(max_length=200, verbose_name='Маркировка')

    def __str__(self):
        return self.equipment_type

    class Meta:
        verbose_name = 'тип оборудования'
        verbose_name_plural = 'Типы оборудования'


class OperationSpecification(models.Model):
    """
    Спецификация операции
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Изделие', default=Product.DEFAULT_PK)
    num = models.IntegerField(verbose_name='Порядковый номер', default=1)
    operation = models.CharField(max_length=200, verbose_name='Операция', default='Введите операцию')
    equipment_type = models.ForeignKey(EquipmentType, on_delete=models.CASCADE,
                                       verbose_name='Тип оборудования', blank=True, null=True)
    operation_time = models.DateTimeField(verbose_name='Время на операцию', default=timezone.now, blank=True)
    description = models.TextField(blank=True, null=True, verbose_name='Описание')

    def __str__(self):
        return self.operation

    class Meta:
        verbose_name = 'спецификация операции'
        verbose_name_plural = 'Спецификации операции'


class Equipment(models.Model):
    """
    Оборудование
    """
    DEFAULT_PK = 1
    marking = models.CharField(max_length=200, verbose_name='Маркировка', default='Введите маркировку')
    equipment_type = models.ForeignKey(EquipmentType, on_delete=models.CASCADE,
                                       verbose_name='Тип оборудования')
    characteristic = models.TextField(blank=True, verbose_name='Характеристика')

    def __str__(self):
        return str(self.equipment_type)

    class Meta:
        verbose_name = 'оборудование'
        verbose_name_plural = 'Оборудование'


class Order(models.Model):
    """
    Заказ
    """
    NEW = 'Новый'
    REJECTED = 'Отменён'
    SPEC = 'Составление спецификации'
    COMFIRMATION = 'Подтверждение'
    PURCHASE = 'Закупка'
    CONTROL = 'Контроль'
    DONE = 'Готов'
    COMPLETED = 'Выполнен'

    STATUS = [
        (NEW, 'Новый'),
        (REJECTED, 'Отменён'),
        (SPEC, 'Составление спецификации'),
        (COMFIRMATION, 'Подтверждение'),
        (PURCHASE, 'Закупка'),
        (CONTROL, 'Контроль'),
        (DONE, 'Готов'),
        (COMPLETED, 'Выполнен'),
    ]
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='Дата заказа')
    order_name = models.CharField(max_length=200, verbose_name='Наименование заказа')
    status = models.CharField(max_length=200, choices=STATUS, verbose_name='Статус заказа',
                              default=NEW)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Изделие',
                                default=Product.DEFAULT_PK)
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                 related_name="customer", verbose_name='Заказчик')
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                related_name="manager", verbose_name='Ответственный менеджер', null=True, blank=True)
    cost = models.FloatField(verbose_name='Стоимость')
    completion_date = models.DateTimeField(verbose_name='Плановая дата завершения', null=True, blank=True)
    work_examples = models.CharField(max_length=200, verbose_name='Примеры работ', null=True, blank=True)

    def __str__(self):
        return '{} {}'.format(self.order_name, self.product)

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'Заказы'


class Tool(models.Model):
    """
    Инструменты
    """
    name = models.CharField(max_length=50, default='Введите наименование инструмента', verbose_name='Наименование')
    description = models.TextField(blank=True, verbose_name='Описание')
    tool_type = models.CharField(max_length=50, default='Введите тип инструмента', verbose_name='Тип инструмента')
    wear_degree = models.CharField(max_length=50, default='Введите степень износа', verbose_name='Степень износа')
    purchase_date = models.DateTimeField(verbose_name='Дата приобретения')
    amount = models.FloatField(default=0, verbose_name='Количество')

    def was_published_recently(self):
        return self.purchase_date >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'purchase_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Приобретено недавно?'

    class Meta:
        verbose_name = 'инструмент'
        verbose_name_plural = 'Инструменты'


class EquipmentFailures(models.Model):
    """
    Сбои оборудования
    """
    CAUSE1 = 'Причина 1'
    CAUSE2 = 'Причина 2'
    CAUSE3 = 'Причина 3'

    CAUSES = [
        (CAUSE1, 'Причина 1'),
        (CAUSE2, 'Причина 2'),
        (CAUSE3, 'Причина 3'),
    ]
    failure_date = models.DateTimeField(verbose_name='Время начала сбоя')
    causes = models.CharField(max_length=200, choices=CAUSES, verbose_name='Причина сбоя',
                              default=CAUSE1)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, verbose_name='Оборудование',
                                  default=Equipment.DEFAULT_PK)
    failure_date_over = models.DateTimeField(verbose_name='Время продолжения работы', blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.equipment)

    class Meta:
        verbose_name = 'сбой оборудования'
        verbose_name_plural = 'Сбои оборудования'
