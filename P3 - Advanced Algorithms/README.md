# Implementing a Route Planner

In this project you will use A* search to implement a "Google-maps" style route planning algorithm.

These Map objects have two properties you will want to use to implement A* search: intersections and roads

### Intersections

The intersections are represented as a dictionary.

In this example, there are 10 intersections, each identified by an x,y coordinate. The coordinates are listed below. You can hover over each dot in the map above to see the intersection number.

### Roads

The roads property is a list where, if i is an intersection, roads[i] contains a list of the intersections that intersection i connects to.


## Writing your algorithm

You should open the file student_code.py in another tab and work on your algorithm there. Do that by selecting File > Open and then selecting the appropriate file.

The algorithm you write will be responsible for generating a path like the one passed into show_map above. In fact, when called with the same map, start and goal, as above you algorithm should produce the path [5, 16, 37, 12, 34]

> shortest_path(map_40, 5, 34)
[5, 16, 37, 12, 34]

