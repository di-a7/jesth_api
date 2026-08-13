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
         #    "pidx":"UYUohMgBXRi783PfXsQy8f",
         #    "payment_url":"https://test-pay.khalti.com/?pidx=UYUohMgBXRi783PfXsQy8f",
         #    "expires_at":"2026-08-13T09:27:00.748444+05:45",
         #    "expires_in":1800}
      data = response.json()
      Payment.objects.create(order = order, pidx = data.get('pidx'), total_amount = order.total_price, status = 'Pending')
      return Response(data)
