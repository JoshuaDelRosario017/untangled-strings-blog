from django.urls import path
from django.conf import settings
from . import views
from .views import *
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views


app_name = 'untangled'


urlpatterns = [
    path('', views.loggedIn, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.loginview, name='loginview'),
    path('register/', views.registerview, name='registerview'),
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
    path('editprofile/', views.edit, name='edit'),
    path('edit-profile/', UserEditView.as_view(), name='edit-profile'),
    path('add/saveasdraft/', views.processDraftPost, name='processDraftPost'),
    path('blog/<int:pk>/', blogEntry.as_view(), name='blogEntry'),
    path('like/<int:pk>/', views.like_post, name='like_post'),
    # path('setting', views.setting, name='setting'),
    # path('edit/save', views.save, name='save'),
    # path('register/process', views.registerUser, name='registerUser'),

    #URL for registration
    path('profile/', ProfileView.as_view(), name='ProfileView'),
    path('login/', LoginView.as_view(), name='LoginView'),
    path('register/', UserRegisterView.as_view(), name='register'),
    # path('change-password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html'), name='change-password'),
    path('change-password/', PasswordChange.as_view(template_name='registration/change-password.html'), name='change-password')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)