from django.shortcuts import render, redirect
from .models import UploadedAudio
import audioread
import os
from django.conf import settings
import pydub
from pydub import AudioSegment
from pydub import AudioSegment
# AudioSegment.converter = "D:\\ffmpeg-6.0-full_build\\bin\\ffmpeg.exe"
# AudioSegment.ffmpeg = "D:\\ffmpeg-6.0-full_build\\bin\\ffmpeg.exe"
# AudioSegment.ffprobe ="D:\\ffmpeg-6.0-full_build\\bin\|ffprobe.exe"

# pydub.AudioSegment.ffmpeg = "D:\\ffmpeg-6.0-full_build\\bin\\ffmpeg"
import audioread
import io    


# def get_audio_duration(audio_file):
#     audio_extension = audio_file.name.split('.')[-1]
#     duration = 0
#     mime_type = f"audio/{audio_extension}"
    
#     if audio_extension in ['mp3', 'wav', 'ogg']:
#         with audioread.audio_open(audio_file.temporary_file_path()) as f:
#             duration = f.duration
#     # Handle other audio formats here if needed
#     return duration

def get_audio_duration(audio_file):
    """
    Calculate the duration of an audio file.

    This function calculates the duration of an audio file by extracting its file extension,
    and then using the 'audioread' library to read and analyze the audio content.

    """
    audio_extension = audio_file.name.split('.')[-1]
    duration = 0
    mime_type = f"audio/{audio_extension}"
    
    if audio_extension in ['mp3', 'wav', 'ogg','aac','flac','m4a']:
        with audioread.audio_open(audio_file.temporary_file_path()) as f:
            duration = f.duration
    # Handle other audio formats here if needed
    return duration

    

def get_audio_extension(content_type):
    """
    Get the audio file extension based on its MIME type.

    This function maps the MIME type of an audio file to its corresponding file extension.
    It is used to determine the extension of an audio file for further processing.

    """
    # Map content type to file extension
    mime_to_extension = {
        'audio/mp3': 'mp3',
        'audio/mpeg': 'mp3',
        'audio/wav': 'wav',
        'audio/ogg': 'ogg',
        'audio/aac': 'aac',
        'audio/flac': 'flac',
        'audio/m4a': 'm4a',
        # Add more MIME types and extensions as needed
    }
    return mime_to_extension.get(content_type, 'unknown')


def upload_audio(request):
    """
    Handle the audio file upload and display uploaded files.

    This function handles the audio file upload process. It calculates the total duration of all uploaded audio files
    and checks whether the total duration exceeds 10 minutes. If the total duration is within limits, the function
    saves the uploaded audio files along with their metadata.

    """
    if request.method == 'POST':
        audio_files = request.FILES.getlist('audio_file')
        total_duration = 0
        
        for audio_file in audio_files:
            audio_duration = get_audio_duration(audio_file)
            total_duration += audio_duration
        
        if total_duration > 600:  # 10 minutes in seconds
            warning_message = "Total duration of uploaded files exceeds 10 minutes. The files will not be saved."
            return render(request, 'upload_audio.html', {'warning_message': warning_message})
        else:
            for audio_file in audio_files:
                audio_duration = get_audio_duration(audio_file)
                audio = UploadedAudio(audio_file=audio_file)
                audio.duration = audio_duration
                
                audio.file_size = audio_file.size
                audio_mime_type = audio_file.content_type
                audio_extension = get_audio_extension(audio_mime_type)
                audio.extension = audio_extension
                audio.save()

        uploaded_files = UploadedAudio.objects.all()
        return render(request, 'upload_audio.html', {'uploaded_files': uploaded_files})

    else:
        warning_message = ""
        uploaded_files = []

    return render(request, 'upload_audio.html', {'warning_message': warning_message})










