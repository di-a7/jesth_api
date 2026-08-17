from django.urls import path
from .views import *
urlpatterns = [
   path('khalti/initiate/',PaymentInit.as_view()),
   path('khalti/verify/',PaymentVerificationAPIView.as_view()),
]

