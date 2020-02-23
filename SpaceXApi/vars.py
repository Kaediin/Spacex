
global_launches = []
full_launches = []
showupcoming = True

def setUpcoming(bool):
    global showupcoming
    showupcoming = not showupcoming

def getUpcoming():
    global showupcoming
    return showupcoming

def setGL(launches):
    global global_launches
    global_launches = launches

def setFull(launches):
    global full_launches
    full_launches = launches

def getFull():
    global full_launches
    return full_launches

def getGL():
    global global_launches
    return global_launches

def sort_Upcoming(show_upcoming):
    launches = []
    global showupcoming

    if not show_upcoming:
        setUpcoming(not showupcoming)
        for launch in getGL():
            if not launch.upcoming:
                launches.append(launch)
        setGL(launches)
    else:
        setUpcoming(not showupcoming)
        setGL(getFull())
        return getFull()

    return launches
