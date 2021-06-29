from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse
#from .models import main1
# Create your views here.
#class HomePageView(TemplateView):
	#template_name = 'index.html'
# Create your views here.
def index(request):
	return render(request,'index.html')
