from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Coupons(models.Model):
    domain = models.CharField(max_length=200, null=False, blank=False)
    coupon_value = models.IntegerField(null=False, blank=False,
                                       validators=[MaxValueValidator(99), MinValueValidator(0)])
    coupon_code = models.CharField(max_length=200, null=False, blank=False)


class SentCoupons(models.Model):
    domain = models.CharField(max_length=200, null=False, blank=False)
    coupon_value = models.IntegerField(null=False, blank=False,
                                       validators=[MaxValueValidator(99), MinValueValidator(0)])
    coupon_code = models.CharField(max_length=200, null=False, blank=False)
