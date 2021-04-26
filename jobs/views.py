from django.shortcuts import render
from .models import Language, Framework, Project, Academic, Profile

# Create your views here.
def home(request):
    language=Language.objects.all().prefetch_related('framework_set')
    project=Project.objects.all().prefetch_related('frameworks')
    academic=Academic.objects.all()
    profile=Profile.objects.latest('pub_date')
    return render(request,'jobs/home.html', {'language':language, 'project':project, 'academic':academic, 'profile':profile})

def resume(request):
    return render(request,'jobs/resume.html')
