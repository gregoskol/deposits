from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Account(models.Model):
    title = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Счет"
        verbose_name_plural = "Счета"

    def __str__(self):
        return self.title


class ActiveType(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Тип актива"
        verbose_name_plural = "Типы активов"

    def __str__(self):
        return self.name


class Active(models.Model):
    name = models.CharField(max_length=15)
    description = models.CharField(max_length=200)
    date_of_buy = models.DateField()
    price_of_buy = models.FloatField()
    sum_price = models.FloatField(blank=True, null=True)
    amount = models.IntegerField()
    type = models.ForeignKey(
        ActiveType,
        on_delete=models.SET_NULL,
        related_name="actives",
        blank=True,
        null=True,
    )
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="actives"
    )
    account = models.ForeignKey(
        Account,
        on_delete=models.SET_NULL,
        related_name="active",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Актив"
        verbose_name_plural = "Активы"

    def __str__(self):
        return self.name
