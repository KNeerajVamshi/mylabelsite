from django.urls import include
from .views import image_upload_view
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include



urlpatterns= [
    path('upload/', image_upload_view),
]