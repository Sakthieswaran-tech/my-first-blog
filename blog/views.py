from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.http import HttpResponse
def post_list(request):
   return render(request,'blog/post_list.html',{'name':'Sakthi'})
def add(request):
      # if request.method=='post':
      #    form = ContactForm(request.POST)
      #    if form.is_valid():
   val1 = int(request.POST['num1'])
   val2 = int(request.POST['num2'])
   res = val1+val2
   return render(request,'blog/result.html',{'result':res})

# Create your views here.
