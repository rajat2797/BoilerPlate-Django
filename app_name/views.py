from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
import requests
import os

# Create your views here.

def index(request):
	return HttpResponse('Hi')