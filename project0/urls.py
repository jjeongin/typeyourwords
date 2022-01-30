from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    path('', views.input_bar, name='home'),
    path('<int:pk>/', views.output_image, name='output_image'),
    path('archive/', views.output_list, name='archive'),
    path('about/', views.about_page, name='about'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)