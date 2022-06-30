from graph import graph
from truck import truck1, truck2, truck3
from pprint import pprint


def get_distance(address1, address2):
    return graph.edge_weights[address1, address2]


def total_miles(route):
    miles = 0
    for i in range(0, len(route) - 1):
        print(f"{route[i]} -> {route[i+1]} = {get_distance(route[i], route[i+1])} miles")
        miles = miles + get_distance(route[i], route[i + 1])
    print(f"Total Miles: {miles}")
    return miles

def nn_sort(route):
    hub = "4001 South 700 East"  # Initialize the starting point
    sorted_route = [hub]    # Initialize sorted route with starting point (hub)

    while route:  # while route list is not empty
        closest = [None, hub]  # Initialize placeholder for closest [distance, location] from current address
        for destination_address in route:  # Iterate through addresses in truck route
            current_address = sorted_route[-1]  # Current address to measure distance from is last item in sorted_route
            distance = get_distance(current_address, destination_address)
            if closest[0] is None:  # Initialize closest [distance, address] to the first destination address
                closest = [distance, destination_address]
            if distance < closest[0]:  # Set closest [distance, address] if distance between addresses is smaller
                closest = [distance, destination_address]
        if closest[1] not in sorted_route:  # Add address to sorted_route
            sorted_route.append(closest[1])
        route.remove(closest[1])    # Remove current location from route list
    sorted_route.append(hub)  # Return to hub sorted_route is complete
    return sorted_route


if __name__ == "__main__":
    optimal_route = nn_sort(truck3.route)
    pprint(optimal_route)
    total_miles(optimal_route)
