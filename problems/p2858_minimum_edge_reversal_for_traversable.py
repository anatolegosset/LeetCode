class Solution:
    def minEdgeReversals(self, n: int, edges: list[list[int]]) -> list[int]:
        edges.sort(key=lambda x: x[1])
        graph = {i: [] for i in range(n)}
        for edge in edges:
            graph[edge[0]].append([True, edge[1]])
            graph[edge[1]].append([False, edge[0]])

        initial_result = 0
        to_visit = [0]
        visited = [False] * n
        visited[0] = True
        while to_visit:
            current_node = to_visit.pop()
            for child in graph[current_node]:
                if not visited[child[1]]:
                    initial_result += not child[0]
                    to_visit.append(child[1])
                    visited[child[1]] = True

        result = [-1] * n
        result[0] = initial_result

        to_visit = [0]
        while to_visit:
            current_node = to_visit.pop()
            for child in graph[current_node]:
                if result[child[1]] == -1:
                    result[child[1]] = result[current_node] + 2 * child[0] - 1
                    to_visit.append(child[1])
        return result




