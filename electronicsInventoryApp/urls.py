"""electronicsInventoryApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import include, path

admin.site.site_header  =  "Electronics Lab"  
admin.site.site_title  =  "Electronics Lab Admin Portal"
admin.site.index_title  =  "Welcome to Electronics Lab Admin Portal"

urlpatterns = [
    path('', include('mainpage.urls')),
    path('admin/', admin.site.urls),
]

from django.conf.urls import handler400, handler403, handler404, handler500


# Customizing the built error pages
handler404 = 'mainpage.views.error_404'
handler500 = 'mainpage.views.error_500'
handler403 = 'mainpage.views.error_403'
handler400 = 'mainpage.views.error_400'
