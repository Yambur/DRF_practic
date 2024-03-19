from django.contrib.auth.models import AbstractUser
from django.db import models

from classes.models import Course, Lesson

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')
    phone = models.CharField(max_length=35, verbose_name='Телефон', **NULLABLE)
    city = models.CharField(max_length=50, verbose_name="Город", **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class Payment(models.Model):

    PAYMENT_METHOD_CHOICES = [
        ('CASH', "Наличные"),
        ('BANK', "Перевод")
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    date_payment = models.DateField(verbose_name="Дата оплаты", **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Оплаченный курс", **NULLABLE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name="Оплаченный урок", **NULLABLE)
    amount = models.IntegerField(max_length=15, verbose_name="Сумма оплаты", **NULLABLE)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES, verbose_name="Метод оплаты",
                                      **NULLABLE)

class Meta:
    verbose_name = "Платеж"
    verbose_name_plural = "Платежи"
