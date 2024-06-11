def graph_coloring(graph, num_colors):
    color = [0] * len(graph)

    def backtrack(vertex):
        if vertex == len(graph):
            return True
        for c in range(1, num_colors + 1):
            if all(color[neighbor] != c for neighbor in graph[vertex]):
                color[vertex] = c
                if backtrack(vertex + 1):
                    return True
                color[vertex] = 0
        return False

    if not backtrack(0):
        print("No solution exists.")
        return False
    print("Solution Exists: ", color)
    return True

# Example Usage:
graph = [[1, 2, 3],
         [0, 2],
         [0, 1, 3],
         [0, 2]]
num_colors = 3
graph_coloring(graph, num_colors)
