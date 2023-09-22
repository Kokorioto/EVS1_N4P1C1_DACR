from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def VISTA1(request):
    html="""
        <h1>Hola</h1>
        <h2>Esta</h2>
        <h3>Es</h3>
        <h4>La vista 1</h4>
        """
    
    return HttpResponse(html)

def VISTA2(request):
    html="""
        <h4>Hola</h4>
        <h3>Esta</h3>
        <h2>Es</h2>
        <h1>La vista 2</h1>
        """
    
    return HttpResponse(html)