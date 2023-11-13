import matplotlib.pyplot as plt
import math
import time

MAX_CITIES_LIMIT = 10
MAX_X_VAL = 100
MAX_Y_VAL = 100
cityList = []

coords = {
    1: (10, 50),
    2: (34, 22),
    3: (63, 1),
    4: (40, 40),
    5: (73, 16),
    6: (57, 68),
    7: (70, 50),
    8: (16, 90),
    9: (95, 57),
    10: (30, 100)
}

# city position object 
class City: 
    def __init__(self, x, y, iVal, visited): 
        self.x = x 
        self.y = y
        self.iVal = iVal
        self.visited = visited


# distance from city a -> b 
def getCityDistance(a, b):
    return math.sqrt(((a.x - b.x) ** 2) + ((a.y - b.y) ** 2))


# create dataset
def dataCreate(coords):
    for i in range(MAX_CITIES_LIMIT):
        x, y = coords[i+1]
        cityList.append(City(x, y, i, False))


def printData(cityList):
    for i in range(len(cityList)):
        print("(" + str(cityList[i].x) + ", " + str(cityList[i].y) + "): " + str(cityList[i].iVal), end=', ')


def getNearestNeighbor(index):
    nearest = float('inf') # start at infinity
    nearestCity = None
    for i in range(len(cityList)):
        # skip checking itself
        if (i == index):
            pass
        elif (cityList[i].visited == True):
            pass 
        else:
            distance = getCityDistance(cityList[i], cityList[index])
            if (distance < nearest):
                nearest = distance
                nearestCity = cityList[i]
                
    if nearestCity is not None:
        nearestCity.visited = True
                
    return nearestCity


def getTour(Cities):
    start = getNearestNeighbor(0)
    visited = []
    tour = [[], 0]
    visited.append(start)
    next = start

    for i in range(1, len(cityList)):
        currentVert = getNearestNeighbor(next.iVal)
        visited.append(currentVert)
        next = currentVert

    for j in visited: 
        tour[0].append(j.iVal)
        tour[1] += getCityDistance(cityList[tour[0][-1]], cityList[tour[0][0]])
        
    return tour


def showTour(cityList, tour):
    x_vals = [city.x for city in cityList]
    y_vals = [city.y for city in cityList]
    fig, ax = plt.subplots()
    plt.title('TSP Nearest Neighbor Algorithm')
    plt.xlabel('X-coordinate')
    plt.ylabel('Y-coordinate')
    # plot all cities as blue dots
    ax.plot(x_vals, y_vals, 'bo')
    # highlight starting node as green dot with a star marker
    start_node = cityList[tour[0][0]]
    ax.plot(start_node.x, start_node.y, marker='o', color='g', mec='g')
    ax.plot(start_node.x, start_node.y, marker='*', color='k')
    # draw arrows between cities in the tour
    for i in range(len(tour[0])):
        start_city = cityList[tour[0][i]]
        end_city = cityList[tour[0][(i+1)%len(tour[0])]]
        ax.arrow(start_city.x, start_city.y, end_city.x-start_city.x, end_city.y-start_city.y, head_width=2, head_length=3, fc='k', ec='k')
    plt.show()




def main():
    dataCreate(coords)
    print("\n")
    startTime = time.time()
    tour = getTour(cityList)
    endTime = time.time()
    print("Nearest Neighbor tour cost: " + str(tour[1]))
    print("Time Elapsed: " + str(round(endTime - startTime, 6)) + " seconds")
    showTour(cityList, tour)

main()

