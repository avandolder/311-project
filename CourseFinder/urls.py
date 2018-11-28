from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from finder import views
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView

urlpatterns = [
    #redirect runserver page to login
    url(r'^$', RedirectView.as_view(url='/login')),

    path('finder/', include('finder.urls')),
    path('admin/', admin.site.urls),
    url('signup/', views.signup),
    path('login/', auth_views.LoginView.as_view(template_name='finder/login.html')),
    url('logout/', views.logout),
    path('profile/', views.profile),
    path('search/', views.search),
    path('faqs/', views.faqs),
    path('profile/paths/', views.paths),
    path('courseinfo/', views.courseinfo)
]
