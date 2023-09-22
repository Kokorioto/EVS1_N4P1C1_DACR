from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def viewone(request):

    html="""
        <h3>Esta es </h3>
        <h1>THE VIEW ONE </h1>
        <h4>De la  </h4>
        <h2>App 2 </h2>
        """
    return HttpResponse (html)

def viewtwo(request):

    html="""
        <h3>Esta es </h3>
        <h1>THE SECOND VIEW </h1>
        <h4>De la  </h4>
        <h2>App 2 </h2>
        """
    return HttpResponse (html)