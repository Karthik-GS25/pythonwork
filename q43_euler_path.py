"""43. Find an Euler path in an undirected graph (Hierholzer)."""


def euler_path(edges):
    graph = {}
    for a, b in edges:
        graph.setdefault(a, []).append(b)
        graph.setdefault(b, []).append(a)
    odd = [v for v in graph if len(graph[v]) % 2]
    if len(odd) not in (0, 2):
        return None
    stack = [odd[0] if odd else next(iter(graph), None)]
    path = []
    while stack:
        v = stack[-1]
        if graph.get(v):
            u = graph[v].pop()
            graph[u].remove(v)
            stack.append(u)
        else:
            path.append(stack.pop())
    return path[::-1] if len(path) == len(edges) + 1 else None


print(euler_path([(1, 2), (2, 3), (3, 1)]))
