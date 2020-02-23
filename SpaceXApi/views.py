from django.shortcuts import render
import urllib.request
import json
from django.http import JsonResponse


# Create your views here.
# importing the requests library

def spaceXApi(request):
    url = 'https://api.spacexdata.com/v3/launches'
    response = urllib.request.urlopen(url).read()
    json_obj = str(response, 'utf-8')
    data = json.loads(json_obj)

    counter = 0
    size = []
    mission_names = []
    rocket_names = []
    launch_dates_local = []
    images = []
    description = []


    for launch in data:
        size.append(counter)
        mission_names.append(launch['mission_name'])
        rocket_names.append(launch['rocket']['rocket_name'])
        launch_dates_local.append(launch['launch_date_local'])
        images.append(launch['links']['mission_patch_small'])
        description.append(launch['details'])
        counter += 1

    return render(request, 'index.html', {
        'length': size,
        'size': data.__len__(),
        'mission_names': mission_names,
        'rocket_names': rocket_names,
        'launch_dates_local': launch_dates_local,
        'images': images,
        'description': description,
    })


