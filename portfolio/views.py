from django.shortcuts import render, get_object_or_404
from .models import Project, profile


def projects(request):
    projects = Project.object.all()
    return render(request, 'projects.html', {'projects': projects})



def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, "project_detail.html", {'project': project})


def profile(request):
    profile = profile.objects.first()
    return render(request, 'profile.html', {'profile': profile})