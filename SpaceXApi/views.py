from django.shortcuts import render
from SpaceXApi.models import Launch
from SpaceXApi.vars import *
import urllib.request
import json



# Create your views here.
def getLaunches():
    url = 'https://api.spacexdata.com/v3/launches'
    response = urllib.request.urlopen(url).read()
    json_obj = str(response, 'utf-8')
    data = json.loads(json_obj)

    launches = []

    for info in data:
        # if hide_upcoming:
        # if bool(info['upcoming'] == False):
        launch = Launch(
            info['mission_name'],
            info['rocket']['rocket_name'],
            info['details'],
            info['launch_date_local'],
            info['links']['mission_patch_small'],
            bool(info['upcoming']))
        launches.append(launch)
    # else:
    #     launch = Launch(info['mission_name'], info['rocket']['rocket_name'], info['details'],
    #                     info['launch_date_local'], info['links']['mission_patch_small'], bool(info['upcoming']))
    #     launches.append(launch)
    return launches

sort_old = True

def sortLaunches(request):
    global sort_old
    if (request.POST.get('sort_old')):
        if sort_old:
            launches = getGL()
            setGL(launches)
            sort_old = True
            print('Already sorted old')
        else:
            launches = getGL()
            launches.reverse()
            sort_old = True
            setGL(launches)
            print('sort old')
    else:
        if sort_old:
            launches = getGL()
            launches.reverse()
            sort_old = False
            setGL(launches)
            print('sort new')
        else:
            launches = getGL()
            setGL(launches)
            sort_old = False
            print('Already sorted new')

    return render(request, 'index.html', {
        'launches': launches
    })

def sortUpcoming(request):
    print('sorting')
    if getUpcoming():
        launches = sort_Upcoming(False)
        print(showupcoming)
    else:
        launches = getLaunches()

    return render(request, 'index.html', {
        'show_upcoming': False,
        'launches': launches
    })


def spaceXApi(request):
    setGL(getLaunches())
    setFull(getLaunches())
    return render(request, 'index.html', {
        'show_upcoming': showupcoming,
        'launches': getGL(),
    })
