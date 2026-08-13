from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order
from django.core.mail import send_mail
from django.core.mail import EmailMessage


@receiver(post_save, sender=Order)
def order_created(sender, instance, **kwargs):
      print("New Order Created.")
      # send_mail(
      #    subject='Order Created!',
      #    message='New Order created',
      #    from_email='admin@gmail.com',
      #    recipient_list=['user1@example.com'],
      #    fail_silently=False,
      # )
      
      message = EmailMessage(
            subject="You are awesome!",
            body="Congrats for sending test email with Mailtrap!",
            from_email="hello@example.com",
            to=["shtdia0@gmail.com"],
            reply_to=["support@example.com"],
      )
      message.esp_extra = {
            "category": "Integration Test",
            "custom_variables": {"test_variable": "abc"},
      }
      message.send()

