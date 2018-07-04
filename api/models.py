from django.db import models

class Currency(models.Model):
    """Class represents currency record stored in DB"""
    date_created = models.DateTimeField(auto_now=True)
    symbol = models.CharField(max_length=3, blank=False, unique=True)
    ecb_rate = models.FloatField(default=1.0)

    def __str__(self):
        """Human readible representation of the record"""
        return "{}: {}".format(self.symbol, self.ecb_rate)