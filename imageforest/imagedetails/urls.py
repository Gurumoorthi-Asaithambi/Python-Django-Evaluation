from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
      path('', views.login_user, name="login_user"),
      path('display/', views.display, name='display'),
      path('success/', views.success, name='success'), 
      path('uploadimage/', views.upload_image, name='upload_image'),
      path('search_image/',views.SearchImage , name='search_image'),
      path('register/', views.register, name='register'),
      path('logout_user/', views.logout_user, name='logout_user'), 
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)