"""13. Cheapest flight with at most k stops."""


def cheapest_price(n, flights, src, dst, k):
    cost = [float("inf")] * n
    cost[src] = 0
    for _ in range(k + 1):
        new = cost[:]
        for a, b, price in flights:
            if cost[a] != float("inf"):
                new[b] = min(new[b], cost[a] + price)
        cost = new
    return -1 if cost[dst] == float("inf") else cost[dst]


print(cheapest_price(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1))
