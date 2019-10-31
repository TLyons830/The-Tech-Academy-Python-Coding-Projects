from django.db import models


class Information(models.Model):
    First_Name = models.CharField(max_length=100, default="", blank=True, null=False)
    Last_Name = models.TextField(max_length=100, default="", blank=True, null=False)
    Deposit = models.DecimalField(default=0.00, max_digits=10000, decimal_places=2)

    objects = models.Manager()

    def __str__(self):
        return self.First_Name


TYPE_CHOICES = {
    ('appetizers', 'appetizers'),
    ('entrees', 'entrees'),
    ('treats', 'treats'),
    ('drinks', 'drinks'),
}


class Accounts(models.Model):
    account = models.CharField(max_length=60, choices=TYPE_CHOICES)

    objects = models.Manager()

    def __str__(self):
        return self.account

