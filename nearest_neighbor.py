from graph import graph
from truck import truck1_packages, truck1


def get_distance(address1, address2):
    """
    Returns edge weight (distance) between two addresses
    :param address1:
    :param address2:
    :return: distance
    """
    return graph.edge_weights[address1, address2]


def nn_sort(route):
    hub = "4001 South 700 East"
    sorted_route = [hub]

    while route:  # while route list is not empty
        min = [0, hub]  # Initialize minimum values
        for address in route:
            current_address = sorted_route[-1]
            distance = get_distance(current_address, address)
            if min[0] == 0:
                min = [distance, address]
            if distance < min[0] and distance != 0:
                min = [distance, address]
        if min[1] not in sorted_route:
            sorted_route.append(min[1])
        route.remove(min[1])
    sorted_route.append(hub)  # Return to hub sorted_route is complete
    return sorted_route


if __name__ == "__main__":
    # print(truck1_packages)
    print(truck1.route)
    # print(graph.edge_weights)
    print(nn_sort(truck1.route))
    print(len(nn_sort(truck1.route)))
