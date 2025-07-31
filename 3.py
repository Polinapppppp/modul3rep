def bfs(graph, start):
    visited=[]
    queue=[start]

    while queue:
        vertex=queue.pop(0)
        if vertex not in visited:
            visited.append(vertex)
            print(vertex, end=" ")

            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)


graph={
    1:[2,3],
    2: [1, 4],
    3: [1, 5],
    4: [2],
    5: [3],
}

bfs(graph,1)