import graph


# Nearest neighbor algorithm to determine the delivery route for each package
def nearest_neighbor(truck_route):
    Hub = '4001 South 700 East'  # Sets a start and end location for each Truck

    graph_edge_weight = graph.graph.edge_weight
    locations_to_visit = truck_route.route
    visited_vertex = [Hub]  # List of the locations visited

    # Algorithm to determine which location is the closest to the current location and then go there
    # Runs through the algorithm while there are still locations that need to be visited
    # The last value in the locations_to_visit list is checked with the other addresses in the truck route list
    # The distance for each edge pair is found and the value is set to the distance value
    # The first if statement accounts for the both Vertex's to be the same
    # The second if statement checks to see if any edge value pair is lower than a previous edge value
    # If the edge weight is a smaller value than the address is updated to be one with the smallest value
    # The algorithm runs until all the address are checked
    # The address with the lowest distance value from the previous location is removed from the locations_to_visit
    # list and the visited_vertex list is appended with the address that was removed
    # Time Complexity O(N^2)
    # Space Complexity O(N)
    while len(locations_to_visit) != 0:
        min_dist = 100
        location = " "
        for address in locations_to_visit:
            distance = (graph_edge_weight[visited_vertex[-1], address])  # get the address from the most recently
            if distance == 0:
                min_dist = distance
                location = address
            if distance < min_dist:
                min_dist = distance
                location = address
        visited_vertex.append(location)
        locations_to_visit.remove(location)
    # Adds the return back to the hub after all the locations have been visited
    visited_vertex.append(Hub)
    # Returns the visited_vertex list when the function is called
    return visited_vertex
