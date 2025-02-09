import copy
from collections import defaultdict, deque


class Graph:
    def __init__(self):
        self.graph = defaultdict(dict)

    def add_edge(self, u, v, capacity):
        self.graph[u][v] = capacity
        self.graph[v][u] = 0

    def bfs(self, source, sink, parent):
        visited = set()
        queue = deque([source])
        visited.add(source)

        while queue:
            current = queue.popleft()

            for neighbor, capacity in self.graph[current].items():
                if neighbor not in visited and capacity > 0:
                    queue.append(neighbor)
                    visited.add(neighbor)
                    parent[neighbor] = current
                    if neighbor == sink:
                        return True

        return False

    def edmonds_karp(self, source, sink):
        parent = {}
        max_flow = 0

        while self.bfs(source, sink, parent):
            path_flow = float('Inf')
            s = sink

            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            max_flow += path_flow

            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow


graph = Graph()
edges = [  # T - Terminal; W - Warehouse; S - Store
    ("T1", "W1", 25), ("T1", "W2", 20), ("T1", "W3", 15),
    ("T2", "W3", 15), ("T2", "W4", 30), ("T2", "W2", 10),
    ("W1", "S1", 15), ("W1", "S2", 10), ("W1", "S3", 20),
    ("W2", "S4", 15), ("W2", "S5", 10), ("W2", "S6", 25),
    ("W3", "S7", 20), ("W3", "S8", 15), ("W3", "S9", 10),
    ("W4", "S10", 20), ("W4", "S11", 10), ("W4", "S12", 15),
    ("W4", "S13", 5), ("W4", "S14", 10)
]

for u, v, capacity in edges:
    graph.add_edge(u, v, capacity)

terminals = ["T1", "T2"]
stores = ["S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10", "S11", "S12", "S13", "S14"]

results = []
for terminal in terminals:
    for store in stores:
        temp_graph = copy.deepcopy(graph)
        max_flow = temp_graph.edmonds_karp(terminal, store)
        results.append((terminal, store, max_flow))

print("{:<10} {:<10} {:<10}".format("Terminal", "Store", "Max Flow"))
print("-" * 30)
for terminal, store, flow in results:
    print("{:<10} {:<10} {:<10}".format(terminal, store, flow))