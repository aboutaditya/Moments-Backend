
from django.db import models
import uuid
import qrcode
from io import BytesIO
from django.core.files import File
from django.contrib.auth.models import User

class Event(models.Model):
    name = models.CharField(max_length=255)
    event_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)  # Tracks who created the event

    def save(self, *args, **kwargs):
        if not self.qr_code:
            self.qr_code = self.generate_qr_code()
        super().save(*args, **kwargs)
    
    def generate_qr_code(self):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(f"http://your-domain.com/events/{self.event_id}")  # Link to event's unique URL
        qr.make(fit=True)
        
        img = qr.make_image(fill="black", back_color="white")
        blob = BytesIO()
        img.save(blob, 'PNG')
        return File(blob, name=f'{self.name}_qr_code.png')

    def __str__(self):
        return f"{self.name} by {self.creator.username}"

class Photo(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='photos')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Photo by {self.user.username} in {self.event.name}"
