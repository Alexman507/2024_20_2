from django.urls import path

from main.apps import MainConfig
from main.views import home, product_pk

app_name = MainConfig.name

urlpatterns = [
    path('', home),
    path('products/<int:pk>', product_pk, )
]
