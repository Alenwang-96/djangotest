from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index_view(request):
    return HttpResponse('这是音乐主页')