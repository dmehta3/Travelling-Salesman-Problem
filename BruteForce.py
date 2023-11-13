import matplotlib.pyplot as plt
import math
import time

iterator = []
max = 10

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

def setMatrix(num):
    cost_matrix = {}
    k = num + 1
    for i in range(1, k):
        for j in range(1, k):
            if i == j:
                cost_matrix[(i, j)] = 0
            else:
                cost_matrix[(i, j)] = math.sqrt((coords[i][0]-coords[j][0])**2 + (coords[i][1]-coords[j][1])**2)
    return cost_matrix

numC = setMatrix(max)


def getCost(r, c, input):
    if c == 0:
        c = input
        return math.sqrt((coords[r][0]-coords[c][0])**2 + (coords[r][1]-coords[c][1])**2)
    return numC[(r, c)]

def functionTSP(main, input, arr, resultCity):
    if len(arr) == 1:
        result = getCost(input, arr[0], main) + getCost(arr[0], 0, main)
        return result
    else:
        Distances = []
        for city in arr:
            darr = arr[:]
            darr.remove(city)
            Distances.append(getCost(input, city, main) + functionTSP(main, city, darr, city))
        iterator.append(Distances)
        return min(Distances)

startTime = time.time()
result = functionTSP(1, 1, [2, 3, 4, 5, 6, 7, 8, 9, 10], 1) + getCost(10, 1, 1)
endTime = time.time()

print("\n")
print("Brute force tour cost: " + str(result))
print("Time Elapsed: " + str(round(endTime - startTime, 6)) + " seconds")
x_vals = [coords[i][0] for i in range(1, max+1)]
y_vals = [coords[i][1] for i in range(1, max+1)]

fig, ax = plt.subplots()
plt.title('TSP Brute Force Algorithm')
plt.xlabel('X-coordinate')
plt.ylabel('Y-coordinate')
ax.plot(x_vals, y_vals, 'bo')

for i in range(max):
    start_coord = coords[i+1]
    end_coord = coords[(i+1)%max+1]
    ax.arrow(start_coord[0], start_coord[1], end_coord[0]-start_coord[0], end_coord[1]-start_coord[1], head_width=2, head_length=3, fc='k', ec='k')

ax.plot(coords[1][0], coords[1][1], 'go')
ax.plot(coords[1][0], coords[1][1], 'k*')
ax.plot([coords[1][0], coords[10][0]], [coords[1][1], coords[10][1]], 'k:')
plt.show()
