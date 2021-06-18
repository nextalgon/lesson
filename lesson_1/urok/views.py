from django.shortcuts import render, redirect
from .forms import PupilForm, ClassroomForm
from .models import Classroom, Pupil
from django.core.paginator import Paginator
from django.views.generic import DetailView


def index(request):
    return render(request, 'urok/index.html')


def pupil(request):
    if request.method == "POST":
        form = PupilForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PupilForm()
    return render(request, 'urok/pupil.html', {'form': form})


def classroom(request):
    if request.method == "POST":
        form = ClassroomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ClassroomForm()
    return render(request, 'urok/classroom.html', {'form': form})


def royxat(request):
    form = Pupil.objects.all()
    return render(request, 'urok/royxat.html', {'forms': form })


def sinflar(request):
    sinfi = Classroom.objects.all()
    links = Pupil
    return render(request, 'urok/sinflar.html', {'sinfi': sinfi, 'links': links})


class Oquch(DetailView):
    model = Pupil
    template_name = 'urok/oquch.html'


def category(request, gradue_id):
    page = request.GET.get('page')
    categ = Classroom.objects.get(pk=gradue_id)
    all_topics = Pupil.objects.filter(gradue=categ)
    paginator = Paginator(all_topics, 10)
    topics = paginator.get_page(page)
    return render(request, 'urok/category.html', {'topics': topics})