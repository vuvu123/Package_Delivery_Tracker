from graph import graph


# Helper function that returns distance between two addresses - O(1)
def get_distance(address1, address2):
    return graph.edge_weights[address1, address2]


# Nearest neighbor sorting algorithm - O(n^2)
# From starting location, find the closest location (shortest distance)
# Closest location becomes the location to measure distance from. (Add location to sorted_route list)
# Chosen location is no longer an available location, remove from route from route list.
# Continue this way until there are no available locations, then
# Return to starting point (Append starting point to sorted_route)
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
