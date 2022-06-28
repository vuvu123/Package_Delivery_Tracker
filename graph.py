import csv


class Graph:
    def __init__(self):
        self.adj_list = {}
        self.edge_weights = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2, weight=None):
        self.edge_weights[(v1, v2)] = weight

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])

    def print_edge_weights(self):
        for vertices in self.edge_weights:
            print(f"{vertices} : {self.edge_weights[vertices]}")


def load_distance_data(filename):
    distance_data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            distance_data.append(row)
    return distance_data


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


graph = create_graph('data/distances.csv')
# graph.print_graph()
graph.print_edge_weights()