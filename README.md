
# Audio Upload Dashboard

The **Audio Upload Dashboard** is a web application built using Django that allows users to upload audio files, view their metadata, and play the uploaded audio files.

## Features
- Upload multiple audio files of various formats (e.g., mp3, wav, ogg).
- Display uploaded audio files in a tabular format with metadata.
- Play uploaded audio files directly from the dashboard.
- Display a warning if the total duration of uploaded files exceeds 10 minutes.
- Convert and display audio file durations in a user-friendly "min, sec" format.
- Display audio file sizes in a human-readable format.
- Use of Django, audioread, and custom template filters.

## Getting Started
### Prerequisites

- Python 3.x
- Django (install using `pip install Django`)

### Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd AudioUploadDashboard
   ```

2. Install the required packages:
    ```
    pip install -r requirements.txt
    ```

3. Run migrations:
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
4. Start the development server:
    ```
    python manage.py runserver
    ```

5. Access the application in your browser at http://localhost:8000/upload/.

## Usage
1. Navigate to the upload page.
2. Choose one or more audio files to upload.
3. Click the "Upload" button.
4. Uploaded files will be listed with metadata and a play button.

## Acknowledgements
Built using Django and audioread.
Uses MediaElement.js for audio playback.

## Approach
The Audio Upload Dashboard is a web application developed using the Django framework, designed to allow users to upload audio files, view their metadata, and play the uploaded audio directly from the dashboard. The project follows the MVT(Model-View-template) architectural pattern.

## Frontend
The frontend is built using HTML, CSS, and MediaElement.js for audio playback. The main template is structured with a form for file upload and a table to display uploaded audio files. The frontend also utilizes custom template filters to convert audio durations into a user-friendly "min, sec" format and display file sizes in a human-readable format.

## Backend
The backend is powered by Django and consists of the following components:

1. Models: The UploadedAudio model is used to store information about the uploaded audio files, including the audio file itself, duration, extension, and file size.

2. Views: The upload_audio view handles the file upload and metadata storage. It calculates the total duration of uploaded audio files and displays a warning if the total duration exceeds 10 minutes.

3. Custom Filters: Custom template filters are used to convert audio durations and display file sizes in a more user-friendly format.

## Audioread and Metadata Extraction
To extract audio file durations, the audioread library is used. The get_audio_duration function reads the audio file using the library and retrieves the duration for supported audio formats (e.g., mp3, wav, ogg). Other details such as file extension and MIME type are extracted using content type mapping.

## Deployment
The application can be deployed locally for development using Django's built-in development server. Deployment to a production environment can be done using platforms like Heroku, AWS, or any other preferred hosting service.

## GitHub and Documentation
The project is version-controlled using Git and hosted on GitHub. The README.md file provides comprehensive documentation on installation, usage, features, and licensing. Proper documentation of functions and explanations of code sections are provided using inline comments and docstrings.

![Screenshot (390)](https://github.com/GauravSighariya/audioLibrary/assets/84697605/2570d756-e503-4cae-beb3-784dfb7a0913)
![Screenshot (391)](https://github.com/GauravSighariya/audioLibrary/assets/84697605/250cfe68-75ce-478e-848d-73e13b325cc5)


## Conclusion
The Audio Upload Dashboard provides a user-friendly interface for uploading, managing, and playing audio files. By leveraging the power of Django and libraries like audioread, the project meets the criteria of coding practices, documentation, and creativity while delivering a functional and attractive web application.
