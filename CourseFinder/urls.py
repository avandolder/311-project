from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from finder import views

urlpatterns = [
    path('finder/', include('finder.urls')),
    path('admin/', admin.site.urls),
    url('signup/', views.signup)
]
