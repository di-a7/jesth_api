from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rms.models import Order
import json
from django.conf import settings
import requests
from .models import Payment
from rest_framework.response import Response
# Create your views here.
class PaymentInit(APIView):
   permission_classes = [IsAuthenticated]
   def post(self, request):
      order_id = request.data.get('order_id')
      order = Order.objects.get(id = order_id)
      payload = json.dumps({
         "return_url": "https://127.0.0.1:8000/payment-success",
         "website_url": "https://127.0.0.1:8000/",
         "amount": order.total_price * 100,
         "purchase_order_id": f"{order.id}",
         "purchase_order_name": f"Order {order.id}",
         }
      )
      headers = {
         'Authorization': f'key {settings.KHALTI_LIVE_KEY}',
         'Content-Type': 'application/json',
      }
      response = requests.request("POST", settings.KHALTI_INITIATE_URL, headers=headers, data=payload)
         # response = {
         #    "pidx":"your_pidc",
         #    "payment_url":"https://test-pay.khalti.com/?pidx=your_pidx",
         #    "expires_at":"2026-08-13T09:27:00.748444+05:45",
         #    "expires_in":1800}
      data = response.json()
      Payment.objects.create(order = order, pidx = data.get('pidx'), total_amount = order.total_price, status = 'Pending')
      return Response(data)

class PaymentVerificationAPIView(APIView):
   permission_classes = [IsAuthenticated]
   
   def post(self, request):
      pidx = request.data.get('pidx')
      payload = json.dumps({
         "pidx": pidx
      })

      headers = {
         'Authorization': f'key {settings.KHALTI_LIVE_KEY}',
         'Content-Type': 'application/json',
      }
      response = requests.request("POST", url=settings.KHALTI_LOOKUP_URL, headers=headers, data=payload)
      response = response.json()
      payment = Payment.objects.get(pidx = pidx)
      if response.get('status') == "Completed":
         payment.status = "Completed"
         payment.transaction_id = response.get('transaction_id')
         payment.order.is_paid = True
         payment.order.save()
      elif response.get("status"):
         payment.status = response.get("status")
      payment.save()
      return Response(response)


# initiate -> pidx, payment_url
# payment_url(pay test creds refer documentation)[success]
# lookup/verify -> pidx POST -> status, transaction_id