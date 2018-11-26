from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from finder import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('finder/', include('finder.urls')),
    path('admin/', admin.site.urls),
    url('signup/', views.signup),
    path('login/', auth_views.LoginView.as_view(template_name='finder/login.html')),
    url('logout/', views.logout)
]
