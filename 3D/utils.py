 

def stateNameToCoords(name):
    return([int(name.split('x')[1].split('y')[0].split('z')[0]), 
            int(name.split('x')[1].split('y')[1].split('z')[0]), 
            int(name.split('x')[1].split('y')[1].split('z')[1])])
