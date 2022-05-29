
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *


# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'


def avatarView(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = StudentForm()
    return render(request, 'home.html', {'form': form})


def uploadok(request):
    return HttpResponse(' upload successful')

# Create your views here.
import os

def gallery(request):
    path="C:\\somedirectory"  # insert the path to your directory
    img_list =os.listdir(path)
    return render('home.html', {'images': img_list})
