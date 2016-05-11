ky=[37.575791, 126.973393]
ak=[37.576576, 126.985322]
kw=[37.571577, 126.976310]
dr=[37.574468, 126.957556]
jr3=[37.572529, 126.990257]

import math
myloc=(37.575791, 126.973393)
locations=[(37.576576, 126.985322),(37.571577, 126.976310),(37.574468, 126.957556),(37.572529, 126.990257)]
def getNearLocation(myLoc,locations):
    dist=[]
    for d in locations:
        dist.append(math.sqrt((myloc[0]-d[0])**2 + (myloc[1]-d[1])**2))
    return min(dist)
    print 'minimum ,min(dist)'
print getNearLocation(myLoc,Locations)
