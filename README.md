# Traveling Salesman Algorithm Comparisons
- We will be implementing 2 different algorithm's to solving the Travelling Salesman Problem

# Team Members: 
- Dhruv Engineer 
- Daksh Mehta 

## How?
One approach we are going to use is the nearest-neighbor approach. This is a greedy
algorithm, where it starts at one city (node) and then connects it with the closest unvisited city, repeating until all cities have been visited and then connects back to the start city.
The other approach will be using Brute Force to solve the problem. For this
approach we would consider one city as the start city and then find the minimum cost
path with that first city being the starting point. We would have to get this cost value for each city from the starting city, which would be done through finding all the subsets.

# Commands needed
`pip install -U matplotlib`
