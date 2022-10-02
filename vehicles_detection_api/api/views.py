from time import sleep
from django.shortcuts import render
from django.http import HttpResponse ,JsonResponse
from .models import GeneratedVoice
import pyttsx3
from django.contrib.sites.models import Site
import uuid
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def audio(request):
    current_site = Site.objects.get_current()
    id=str(uuid.uuid4())
    engine = pyttsx3.init("espeak")
    voices = engine.getProperty('voices')
    for i,v in enumerate(voices):
        print(i)
        print(v.languages)
        print(v.name)
        print(v.age)
    engine.setProperty('voice',voices[16].id) 
    t="Nearest car is 2 meters away"
    audio_url=f'media/voices/{id}.mp3'
    engine.save_to_file(t, audio_url)
    engine.runAndWait()
    return JsonResponse({'audio':str(current_site)+audio_url},safe=False)

