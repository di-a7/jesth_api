from django.db import models
from rms.models import Order
# Create your models here.
class Payment(models.Model):
   order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='payment')
   pidx = models.CharField(max_length=25, unique=True)
   transaction_id = models.CharField(max_length=50, null=True, blank=True)
   total_amount = models.FloatField()
   status = models.CharField(max_length=15, default='Pending')
   
   def __str__(self):
      return f"{self.order.user}- {self.status}"