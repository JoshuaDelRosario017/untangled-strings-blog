from django.urls import path
from django.conf import settings
from . import views
from .views import *
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

app_name = 'untangled'


urlpatterns = [

    path('', views.landingpage, name='landingpage'),
    path('blogs/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/process/', views.process, name='process'),
    path('processlogout/', views.processlogout, name='processlogout'),
    path('create/', login_required(AddPostView.as_view()), name='add'),
    path('publishpost/', views.processAddPost, name='processAddPost'),
    path('published/', views.published, name='published'),
    path('drafts/', views.drafts, name='drafts'),
    path('deleted/', views.deleted, name='deleted'),
    path('addCategory/', views.addCategory, name='addCategory'),
    path('processAddCategory/', views.processAddCategory, name='processAddCategory'),
    path('<int:id>/deleteCategories/', views.deleteCategories, name='deleteCategories'),
    path('profile/', views.profile, name='profile'),
    # path('editprofile/', views.edit, name='edit'),
    path('edit-profile/', UserEditView.as_view(), name='edit-profile'),
    path('add/saveasdraft/', views.processDraftPost, name='processDraftPost'),
    path('blog/<int:pk>/<str:blog_title>', blogEntry.as_view(), name='blogEntry'),
    path('like/<int:pk>/<str:blog_title>', views.like_post, name='like_post'),
    # path('setting', views.setting, name='setting'),
    # path('edit/save', views.save, name='save'),
    # path('untangledstrings/', views.untangledstring, name='untangledstring'),
    path('login/', views.loginview, name='loginview'),
    path('books/', views.booksSection, name='booksSection'),
    # path('capture_image/', capture_image, name='capture_image'),
    # path('display_image/', display_image, name='display_image'),
    # path('register/', views.registerview, name='registerview'),

    #URL for registration
    path('profile/', ProfileView.as_view(), name='ProfileView'),
    # path('login/', LoginView.as_view(), name='LoginView'),
    path('register/', UserRegisterView.as_view(), name='register'),
    # path('change-password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html'), name='change-password'),
    path('change_password/', PasswordChange.as_view(template_name='registration/change-password.html'), name='change-password'),

    # Password Reset URL
    path('password_reset/', PassReset.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),

    # path("robots.txt",TemplateView.as_view(template_name="untangled/robots.txt", content_type="text/plain")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)