from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static

app_name = 'form_app'

urlpatterns = [
  path('', views.index, name='index'),
  path('form_page/', views.form_page, name='form_page'),
  path('form_post/', views.form_post, name='form_post'),
  path('form_set_post/', views.form_set_post, name='form_set_post'),
  path('modelform_set_post/', views.modelform_set_post, name='modelform_set_post'),
  path('upload_sample/', views.upload_sample, name='upload_sample'),
  path('upload_model_form/', views.upload_model_form, name='upload_model_form'),
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
