"""mydjango URL Configuration

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

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('about/', views.about, name="about-page"),
    path('termnco/', views.termnco, name="termnco-page"),
    path('privacy/', views.privacy, name="privacy-page"),
    path('blog/', views.blog, name="blog-list-page"),
    path('blog/<id>/', views.blog_detail, name="blog-detail-page"),
    path('create/', views.blog_create, name="blog-create-page"),
    path('blog/<id>/update/', views.blog_update, name="blog-update-page"),
    path('blog/<id>/delete/', views.blog_delete, name="blog-delete-page"),
    path('tinymce/', include('tinymce.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    """urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)"""