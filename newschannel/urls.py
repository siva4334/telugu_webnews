"""newschannel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webnews import views
from django.views.generic import RedirectView

from django.conf.urls.static import static

from django.conf import settings

urlpatterns = [

	path('favicon\.ico',RedirectView.as_view(url='static/images/favicon.ico')),
    path('admin/', admin.site.urls),
	path('subpage/<str:title>/',views.subpage,name='sub'),
	path('',views.mainpage,name='main'),
	path('national/',views.national,name='national'),
	path('international/',views.international,name='international'),
	path('local/',views.local,name='local'),
	path('cinema/',views.cinema,name='cinema'),
	path('sports/',views.sports,name='sports'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
