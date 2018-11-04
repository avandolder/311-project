from django.urls import path

from . import views

app_name = "finder"
urlpatterns = [
    path('finder/', views.index, name='index'),
]
