from django.urls import include, path
from . import views 

urlpatterns =[
  path('placeorder/',views.placeorder,name='placeorder'),
  path('payments',views.payments,name='payments'),
  path('order_complete/',views.order_complete,name='order_complete'),
]