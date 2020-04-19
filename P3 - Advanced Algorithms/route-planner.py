def distance(a, b) :
#     print(a, b, ( ((a[0] - b[0]) ** 2) + ((a[1] - b[1]) ** 2) ) ** 0.5)
    return ( ((a[0] - b[0]) ** 2) + ((a[1] - b[1]) ** 2) ) ** 0.5

def shortest_path(M,start,goal):
    print("shortest path called")
    n = len(M.intersections)
    current = start
    visited = [False] * n    
    path_costs = [0] * n
    breadcrumbs = [-1] * n
    heap = {}
    goal_coords = M.intersections[goal]
         
    while (current != goal) :
        visited[current] = True
        curr_coords = M.intersections[current]
        for new_road in M.roads[current] :
            if not visited[new_road] :
                coords = M.intersections[new_road]
                f = path_costs[current] + distance(coords, curr_coords) + distance(goal_coords, coords)
                heap[f] = new_road
        
        next = sorted(heap.keys())[0]
        previous =  current
        current = heap.pop(next)  
        next_coords = M.intersections[current]
        if path_costs[current] == 0 :
            path_costs[current] = path_costs[current] + distance(next_coords, curr_coords)
        else: 
            path_costs[current] = min(path_costs[current], path_costs[current] + distance(next_coords, curr_coords))
                     
        breadcrumbs[current] = previous
        breadcrumbs.append(current)      
    
    ans = []
    while current != start :
        ans.append(current)
        current = breadcrumbs[current]
    ans.append(current)
    
    return ans[::-1]