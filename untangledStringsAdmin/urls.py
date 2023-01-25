from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from untangledStringsAdmin.views import *
from untangledStringsAdmin import views


app_name = 'untangledStringsAdmin'

urlpatterns = [
    path('admin-dashboard/', views.adminDashboard, name='adminDashboard')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)