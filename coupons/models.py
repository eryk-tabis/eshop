from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.


class Coupon(models.Model):
    """
    List of properties in Coupon model
    """
    code = models.CharField(max_length=50, unique=True)
    valid_from = models.DateField()
    valid_to = models.DateField()
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    active = models.BooleanField()

    def __str__(self):
        return self.code
