from django.forms import Form
from django.forms import ModelForm
from video.models import Video

class VideoForm(ModelForm): 
    class Meta:
        model = Video
        fields = ['name','url']