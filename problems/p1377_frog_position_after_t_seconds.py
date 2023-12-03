class Solution:
    def frogPosition(self, n: int, edges: list[list[int]], t: int, target: int) -> float:
        if target == 1:
            return float(n == 1)
        graph = {i: [0.0, set()] for i in range(1, n + 1)}
        for edge in edges:
            graph[edge[0]][1].add(edge[1])
            graph[edge[1]][1].add(edge[0])
        graph[1][0] = 1.0
        parents = [1]
        for i in range(1, t + 1):
            children = []
            for parent in parents:
                new_p = graph[parent][0] / (len(graph[parent][1]) or 1)
                for child in graph[parent][1]:
                    graph[child][1].remove(parent)
                    if child == target:
                        return new_p * (i == t or not graph[child][1])
                    graph[child][0] = new_p
                    children.append(child)
            parents = children
        return 0


