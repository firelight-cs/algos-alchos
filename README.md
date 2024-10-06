# algos-alchos
Is a repository where I leave programs that somehow and somewhere can be useful, but actually I practice my algorithms skills

## Breadth-first search (bfs)
In my program, I decided to use the most obvious example of a graph from real life - a subway diagram. I used the Prague's metro scheme, because it is quite simple, but on its example I can see if the algorithm will work at all. 

In general, the script is quite simple: enter a boarding station and a end station, get the shortest path

***INPUT***:
-> Hlavni Nadrazi
-> Malostranska

***OUTPUT***:
['Hlavni Nadrazi', 'Muzeum', 'Mustek', 'Staromestska', 'Malostranska']


## Dijkstra's algorithm
Search algorithm in weighted graph. Finds the shortest distances for every node in graph. 

On this alogrithm I got a little fancy and decided to extend the functionality of the script. In addition to the basic search, I also added path restoring, which was calculated by subtracting values from the dictionary of shortest distances and edge weights for node and it's neighbor. After comparison, we can determine whether a vertex is part of the shortest path or not.

I also decided to add a rough estimate of time, since each edge has a weight, which represents a number that is multiplied by 500 to get the distance in meters between stations (nodes). I also estimated the average speed and based on this data you can already predict the time, as well as not forgetting to add 30 seconds stop at each station

***INPUT***:
-> Hlavni Nadrazi
-> Malostranska

***OUTPUT***:
Estimated time of the trip: 7 minutes

Shortest path look like this: Hlavni Nadrazi -> Muzeum -> Mustek -> Staromestska -> Malostranska
