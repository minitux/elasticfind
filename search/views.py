# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from pyes import *

def index(request):
    conn = ES(['elasticsearch.01net.com:9200'])
   
    q = TermQuery("message", "google")
    results = conn.search(query = q) 

    return render(request, "home/index.html", {'variable': results})
