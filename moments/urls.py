from django.urls import path
from .views import CreateEventView, EventPhotosView, UploadPhotoView, UserRegistrationView,LoginView
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register', UserRegistrationView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('events/create', CreateEventView.as_view(), name='create-event'),
    path('events/<uuid:event_id>/photos', EventPhotosView.as_view(), name='event-photos'),
    path('photos/upload', UploadPhotoView.as_view(), name='upload-photo'),
    path('api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)