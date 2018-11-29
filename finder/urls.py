from django.urls import path
from . import views

app_name = "finder"
urlpatterns = [
    path('', views.index, name='index'),
    path('delete_user', views.delete_user, name='delete_user'),
]
