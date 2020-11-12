GRAPH = [[1, 2], [0, 4, 3], [0, 4], [1, 4, 5], [1, 2, 3, 5], [3, 4]]  # adjacency list
GRAPH1 = [[1, 2, 3], [0, 4], [0, 5, 6], [0, 7], [1, 8], [2, 8], [2, 7], [3, 6], [4, 5]]


def bfs(source, graph=GRAPH):
    visited = [False] * len(graph)
    queue = [source]
    visited[source] = True
    print(source)

    while len(queue) != 0:
        for i in graph[queue[0]]:
            if visited[i] is not True:
                print(i)
                queue.append(i)
                visited[i] = True

        queue.pop(0)


bfs(0, GRAPH1)