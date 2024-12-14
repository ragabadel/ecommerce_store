from django.urls import path
from . import views

urlpatterns = [
    path('<str:link>',views.Dynamic_link, name="Dynamic_link ")
]  