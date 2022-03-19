import datetime

from django.db import models
from django.core import validators
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Tariff(models.Model):
    """
    Модель тарифа. Предполагается, что можно менять все в описании
    (название, дату окончания, пакет минут/cмс/траффика)
    """

    class Meta:
        verbose_name = _('Tariff')
        verbose_name_plural = _('Tariffs')

    name = models.CharField(
        max_length=100, verbose_name=_('Name'), unique=True
    )
    start_date = models.DateField(verbose_name=_('Start date'))
    exp_date = models.DateField(verbose_name=_('Expiration date'))
    minutes_volume = models.IntegerField(
        validators=[validators.MinValueValidator(0)],
        verbose_name=_('Minutes volume'),
    )
    sms_volume = models.IntegerField(
        validators=[validators.MinValueValidator(0)],
        verbose_name=_('SMS volume'),
    )
    traffic_volume = models.IntegerField(
        validators=[validators.MinValueValidator(0)],
        verbose_name=_('Traffic volume'),
    )

    def __str__(self):
        return self.name


class Customer(models.Model):
    """
    Модель абонента. По умолчанию после создания баланс ставится в 0.
    """

    class Meta:
        verbose_name = _('Customer')
        verbose_name_plural = _('Customers')

    balance = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, verbose_name=_('Balance')
    )
    last_action_timestamp = models.DateTimeField(
        auto_now_add=True, verbose_name=_('Timestamp of last activity')
    )
    age = models.IntegerField(
        validators=[validators.MinValueValidator(0)], verbose_name=_('Age')
    )
    city = models.CharField(max_length=60, verbose_name=_('City'))
    created_at = models.DateField(
        auto_now_add=True, editable=False, verbose_name=_('Creation date')
    )
    active_tariff = models.ForeignKey(
        Tariff,
        related_name='customers',
        # Предполагается, что могут быть абоненты,
        # у которых в какой то момент нет тарифа
        on_delete=models.SET_NULL,
        verbose_name=_('Active tariff'),
        blank=True,
        null=True,
    )

    def __str__(self):
        return str(self.id)


class Event(models.Model):
    """
    Модель события.
    """

    class Meta:
        verbose_name = _('Event')
        verbose_name_plural = _('Events')

    class ServiceType(models.TextChoices):
        CALL = 'C', _('Call')
        SMS = 'S', _('SMS')
        TRAFFIC = 'T', _('Traffic')

    timestamp = models.DateTimeField(
        auto_now_add=True, editable=False, verbose_name=_('Timestamp')
    )
    customer = models.ForeignKey(
        Customer,
        related_name='events',
        # Предполагается, что информация об абонентах не будет удаляться.
        # DO_NOTHING ставить не рекомендуется
        on_delete=models.CASCADE,
        verbose_name=_('Customer'),
    )
    service_type = models.CharField(
        max_length=1,
        choices=ServiceType.choices,
        verbose_name=_('Type of service'),
    )
    units_spent = models.IntegerField(
        validators=[validators.MinValueValidator(1)],
        verbose_name=_('Amount of units spent'),
    )

    def __str__(self):
        return f'{self.id}, {self.timestamp}'
