
from django.urls import path
from . import views
from .views import home
from . import views

urlpatterns = [
    path('create/', views.create_profile, name='create_profile'),
    path('edit/<int:profile_id>/', views.edit_profile, name='edit_profile'),
    path('download/pdf/<int:profile_id>/', views.download_pdf, name='download_pdf'),
    path('download/word/<int:profile_id>/', views.download_word, name='download_word'),
    path('', home, name='home'),  # Ana sayfa görünümü
    path('form/<int:template_id>/', views.form_view, name='form'),  # Form sayfası
]
