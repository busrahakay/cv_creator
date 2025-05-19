from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cvapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.welcome, name='welcome'),
    path('templates/', views.index, name='index'),
    path('create/', views.create_cv, name='create_cv'),
    path('list/', views.cv_list, name='cv_list'),
    path('preview/<int:cv_id>/', views.preview_cv, name='preview_cv'),
    path('download/pdf/<int:cv_id>/', views.download_cv_pdf, name='download_cv_pdf'),
    path('download/word/<int:cv_id>/', views.download_cv_word, name='download_cv_word'),
    path('delete/<int:cv_id>/', views.delete_cv, name='delete_cv'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
