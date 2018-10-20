from django.shortcuts import render
from pageapp.models import Video 


# Create your views here.
def listing(request):
    context = {}
    vids_list = Video.objects.all()
    context['vids_list'] = vids_list

