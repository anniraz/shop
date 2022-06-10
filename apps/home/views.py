from django.shortcuts import render
from apps.home.models import Setting


# Create your views here.
def index(request):
    # settings = Setting.objects.latest('id')
    # context = {
    #     'settings': settings, 
    # }
    return render(request, 'index.html', )