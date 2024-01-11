from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Ball

# balls = [
#     {'name': 'Golf Ball', 'brand': 'Titelist', 'size': 'Small'},
#     {'name': 'Basketball', 'brand': 'Wilson', 'size': 'Medium'},
#     {'name': 'Football', 'brand': 'Wilson', 'size': 'Medium'},
#     {'name': 'Baseball', 'brand': 'Rawlings', 'size': 'Small'},
#     {'name': 'Beach Ball', 'brand': 'Intex', 'size': 'Large'},
# ]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def balls_index(request):
    balls = Ball.objects.all()
    return render(request, 'balls/index.html', {
        'balls': balls
    })

def balls_detail(request, ball_id):
    ball = Ball.objects.get(id=ball_id)
    return render(request, 'balls/detail.html', {
        'ball': ball
    })

class BallCreate(CreateView):
    model = Ball
    fields = '__all__'

class BallUpdate(UpdateView):
    model = Ball
    fields = '__all__'

class BallDelete(DeleteView):
    model = Ball
    success_url = '/balls'