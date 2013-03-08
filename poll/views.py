from django.http import HttpResponse
from django.shortcuts import render
from poll.models import Poll

def index(request):
    poll_list = Poll.objects.all()
    return render(request, "home/index.html", {'polls':poll_list})
def detail(request):
    return render(request, "poll/details.html", {'variable': 'Salut Connard'})
