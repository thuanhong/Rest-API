from django.shortcuts import render
from .models import Resource, Method
from django.http import HttpResponse
from .call import *
from json import loads

# Create your views here.
def home(request):
    my_dict = {
        'res' : Resource.objects,
        'method' : Resource.objects.all()[0],
        'default' : Resource.objects.all()[0].id
    }
    return render(request, 'home.html', my_dict)


def run(request, each_id):
    my_dict = {
        'res' : Resource.objects,
        'method' : Resource.objects.get(pk=each_id),
        'default' : each_id
    }
    return render(request, 'home.html', my_dict)


def execute(request, default):
    resource = Resource.objects.get(pk=default).resource
    method = request.POST['choice']

    myDict = dict(request.POST.lists())
    params = get_params(myDict['param_key'], myDict['param_value'])
    headers = get_header(myDict['header_key'], myDict['header_value'])
    try:
        if request.POST['body'] == '':
            body = None
        else:
            body = loads(request.POST['body'])
    except Exception:
        my_dict = {
            'res' : Resource.objects,
            'method' : Resource.objects.get(pk=default),
            'default' : default,
            'error' : "Wrong body format, must is json type or empty"
        }
        return render(request, 'home.html', my_dict)
    output = get_reponse(resource, body, method, headers, params)
    return render(request, 'results.html', {'output':output})

