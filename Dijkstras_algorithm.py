# Алгоритм Дейкстры.

INFINITY = float("inf")

graph = {'start': {'a': 6, 'b': 2}, 'a': {
    'fin': 1}, 'b': {'a': 3, 'fin': 5}, 'fin': {}}
# costs = {'a': 6, 'b': 2, 'fin': INFINITY}
# parents = {'a': 'start', 'b': 'start', 'fin': None}

graph_a = {"start": {'a': 5, 'b': 2},
           'a': {'c': 7, 'd': 2},
           'b': {'a': 8, 'd': 7},
           'c': {'fin': 3, 'd': 6},
           'd': {'fin': 1},
           'fin': {}
           }
graph_b = {"start": {'a': 10},
           'a': {'c': 20},
           'b': {'a': 1},
           'c': {'fin': 30, 'b': 1},
           'fin': {}
           }

graphs = [graph_a, graph_b]
# costs = {'a': 5, 'b': 2, 'c': INFINITY, 'd': INFINITY,  'fin': INFINITY}
# parents = {'a': 'start', 'b': 'start'}


# def result_path(parents, final_node):
#     final_node = final_node
#     reversed_path = [final_node]
#     parent = parents.get(final_node)
#     while parent is not None:
#         reversed_path.append(parent)
#         parent = parents.get(parent)
#     return reversed(reversed_path)


# def find_lowest_cost_node(costs, processed):
#     lowest_cost = INFINITY
#     lowest_cost_node = None
#     for node in costs:
#         cost = costs[node]
#         if cost < lowest_cost and node not in processed:
#             lowest_cost = cost
#             lowest_cost_node = node
#     return lowest_cost_node


# def dijkstars_algorithm(graph, costs, parents):
#     processed = []
#     node = find_lowest_cost_node(costs, processed)
#     while node is not None:
#         cost = costs[node]
#         neighbours = graph[node]
#         for n in neighbours.keys():
#             new_cost = cost + neighbours[n]
#             if costs[n] > new_cost:
#                 costs[n] = new_cost
#                 parents[n] = node
#         processed.append(node)
#         node = find_lowest_cost_node(costs, processed)
#     print("Path: ", " --> ".join(result_path(parents, "fin")))
#     print("Total cost: ", costs["fin"])


class DijkstarsAlgorithm:

    def _get_result_path(self):
        reversed_path = [self.final_node]
        parent = self.parents.get(self.final_node)
        while parent is not None:
            reversed_path.append(parent)
            parent = self.parents.get(parent)
        return reversed(reversed_path)

    def _find_lowest_cost_node(self):
        lowest_cost = INFINITY
        lowest_cost_node = None
        for node, cost in self.costs.items():
            if cost < lowest_cost and node not in self.processed:
                lowest_cost = cost
                lowest_cost_node = node
        return lowest_cost_node

    def _collect_results(self):
        node = self._find_lowest_cost_node()
        while node is not None:
            cost = self.costs[node]
            neighbours = self.graph[node]
            for n, neigh_cost in neighbours.items():
                new_cost = cost + neigh_cost
                if self.costs[n] > new_cost:
                    self.costs[n] = new_cost
                    self.parents[n] = node
            self.processed.append(node)
            node = self._find_lowest_cost_node()
        print("Path: ", " --> ".join(self._get_result_path()))
        print("Total cost: ", self.costs[self.final_node])

    def __call__(self, graph, starting_node, final_node):
        self.processed = []
        self.graph = graph
        self.starting_node = starting_node
        self.final_node = final_node
        self.parents = {n: starting_node for n in graph[starting_node]}
        self.costs = graph[starting_node]
        known_part = [starting_node]
        known_part.extend(self.costs.keys())
        self.costs.update({n: INFINITY for n in graph if n not in known_part})
        self._collect_results()


if __name__ == "__main__":
    # dijkstars_algorithm(graph, costs, parents)
    a = DijkstarsAlgorithm()
    for graph in graphs:
        a(graph, 'start', 'fin')
