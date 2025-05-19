from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('templates/', views.index, name='index'),
    path('create/', views.create_cv, name='create_cv'),
    path('preview/<int:cv_id>/', views.preview_cv, name='preview_cv'),
    path('list/', views.cv_list, name='cv_list'),
    path('delete/<int:cv_id>/', views.delete_cv, name='delete_cv'),
    path('download/word/<int:cv_id>/', views.download_cv_word, name='download_cv_word'),
    path('download/pdf/<int:cv_id>/', views.download_cv_pdf, name='download_cv_pdf'),
]