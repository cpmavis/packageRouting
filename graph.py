import csv


# Creates a class with all the information needed to store the information that is read from the files and
# assign a vertex to the package drop off locations and store distance between each of the package drop off locations
class Graph:  # (Lysecky, 2018)
    def __init__(self):
        self.adjacent_list = {}
        self.edge_weight = {}

    # Add a location into the graph where each package is dropped off (Vertex)
    def add_vertex(self, new_vertex):
        if new_vertex not in self.adjacent_list:
            self.adjacent_list[new_vertex] = []

    # The distance between each package drop off location
    def add_weighted_edge(self, vertex_a, vertex_b, weight=1.0):
        self.edge_weight[(vertex_a, vertex_b)] = weight
        self.adjacent_list[vertex_a].append((vertex_b, weight))


# Reads and extracts the data from the CSV file and creates a new list containing the data
with open('addresses.csv') as csv_file:
    data = csv.reader(csv_file)
    address_csv = list(data)
# Reads and extracts the data from the CSV file and creates a new list containing the data and sets it as type float
with open('WGUPS Distance Table.csv') as csv_file:
    data = csv.reader(csv_file, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
    distance_csv = list(data)

    # creates an instance of the Graph object
    graph = Graph()
    # Reads through each row in the address CSV list and creates a new Vertex for every location
    # Adds the vertex to the graph
    # Second loops creates an edge weight for every pair of address
    # Time Complexity O(N^2)
    # Space Complexity O(1)
    for row in address_csv:
        graph.add_vertex(row[1])  # each vertex is the address for the package to be delivered
    for i in range(len(distance_csv)):
        for j in range(len(distance_csv)):
            graph.add_weighted_edge(address_csv[i][1], address_csv[j][1], distance_csv[i][j])
            # loops through the address list twice to get all possible address edge weights and gets the distance
            # for each pair of addresses

