
infinity = float("inf")

# A weighted graph stored as graph[str: 'name_of_node'][str: 'name of child'] = int: edge weight 
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["meta"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["meta"] = 5
graph["meta"] = {}

# Hash table mapping child to parent in form parent[str: "name_of_child"] = 'name_of_parent'
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["meta"] = None

# Hash table containing the costs to reach different destinations
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["meta"] = infinity

# List containing processed nodes
processed = []

def find_lowest_cost_node(costs):
    lowest_cost = infinity
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
        return lowest_cost_node

node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)

print(parents)
print(costs)
