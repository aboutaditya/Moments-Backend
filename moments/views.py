from rest_framework import generics, permissions, status
from .models import Event, Photo
from .serializers import EventSerializer, PhotoSerializer, UserSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        Token.objects.create(user=user)  # Create a token for the new user

class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)

class CreateEventView(generics.CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only logged-in users can create events

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)  # Automatically set the event creator to the logged-in user

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        # Include the QR code in the response so it can be displayed in the app
        event = Event.objects.get(id=response.data['id'])
        response.data['qr_code'] = event.qr_code.url
        return response

class EventPhotosView(generics.ListAPIView):
    serializer_class = PhotoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        event_id = self.kwargs['event_id']
        return Photo.objects.filter(event__event_id=event_id)

class UploadPhotoView(generics.CreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        event_id = self.request.data.get('event_id')
        event = Event.objects.get(event_id=event_id)
        serializer.save(user=self.request.user, event=event)
