from django.db import models

class UploadedAudio(models.Model):
    audio_file = models.FileField(upload_to='')
    upload_date = models.DateTimeField(auto_now_add=True)
    file_size = models.PositiveIntegerField(blank=True,null=True)
    duration = models.FloatField(blank=True,null=True)  # Duration of the audio in seconds
    extension = models.CharField(max_length=10,blank=True,null=True)

    def __str__(self):
        return self.audio_file.name