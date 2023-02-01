import random
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

def Dijkstra(graph, parents, costs):
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
        return graph, parent, costs

# Generates directed acylic graph
# graph stored as graph[str: 'name_of_node'][str: 'name of child'] = int: edge weight 
def generate_dag(number_of_nodes = 10):
    nodes = [node for node in range((number_of_nodes) - 2)]
    graph = {}
    
    # Starting node can be connected to any of the first 4 nodes.
    graph["start"] = {}
    for connection in range(0, 4):
        random_n = random.randint(0, 1)
        random_value = random.randint(0, 20)
        if random_n == 1:
            graph["start"][connection] = random_value

    # For every next node except the last four
    for node in nodes[:(number_of_nodes - 3)]:
        graph[node] = {}
        
        # The first connection is guaranteed in order not to disconnect the graph
        graph[node][node + 1] = random.randint(0, 20)
        for connection in range(2, 4):
            random_n = random.randint(0, 1)
            random_value = random.randint(0, 20)
            if random_n == 1:
                new_connection = node + connection
                graph[node][new_connection] = random_value
    
    for node in nodes[:(number_of_nodes - 1)]:
        print(node)
    return graph

        
        


graph = generate_dag()
route = {}

#parent = 'meta'
#while parent != 'start':
    #route[parent] = costs[parent]
    #parent = parents[parent]

#for node in route:
    #print(route[node])



