import csv


# Graph data structure was used to hold distance data between addresses
class Graph:
    def __init__(self):
        self.adj_list = {}
        self.edge_weights = {}

    # Adds vertex to adjacency list - O(N)
    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    # Adds an edge to edge_weights dictionary - O(1)
    def add_edge(self, v1, v2, weight=None):
        self.edge_weights[(v1, v2)] = weight


# Helper function returns list of rows of csv data
# O(N)
def load_distance_data(filename):
    distance_data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            distance_data.append(row)
    return distance_data


# Creates graph
# O(N^2)
def create_graph(filename):
    distance_data = load_distance_data(filename)
    graph_distances = Graph()
    for row in distance_data:
        graph_distances.add_vertex(row[0])
        for i, location in enumerate(distance_data):
            origin = row[0]
            destination = distance_data[i][0]
            miles = row[i + 1]
            graph_distances.add_edge(origin, destination, float(miles))
    return graph_distances


# Graph object to be used in other files to measure distance
graph = create_graph('data/distances.csv')

