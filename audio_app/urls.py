from django.urls import path
from .views import upload_audio
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('upload/', upload_audio, name='upload_audio'),
    
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)