from collections import defaultdict, deque

def read_graph_input():
    graph = defaultdict(set)
    while True:
        try:
            line = input().strip()
            if not line:
                break
            node, connections = line.split(':')
            node = node.strip()
            connections = connections.strip()
            if connections:
                for conn in connections.split(','):
                    conn = conn.strip()
                    graph[node].add(conn)
                    graph[conn].add(node)
            else:
                if node not in graph:
                    graph[node] = set()
        except EOFError:
            break
    return graph

def bfs_shortest_path(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = deque([start])
    while queue:
        current = queue.popleft()
        current_distance = distances[current]
        for neighbor in graph[current]:
            if distances[neighbor] == float('inf'):
                distances[neighbor] = current_distance + 1
                queue.append(neighbor)
    return distances

def calculate_metrics(graph):
    vertices = list(graph.keys())
    num_vertices = len(vertices)

    if num_vertices == 0:
        return None

    all_distances = []
    for node in vertices:
        distances = bfs_shortest_path(graph, node)
        all_distances.extend(distances.values())

    # Distância média
    num_distances = len(all_distances)
    average_distance = sum(d for d in all_distances if d < float('inf')) / num_distances

    # Diâmetro
    finite_distances = [d for d in all_distances if d < float('inf')]
    diameter = max(finite_distances) if finite_distances else float('inf')

    # Densidade
    num_edges = sum(len(edges) for edges in graph.values()) // 2
    density = num_edges / (num_vertices * (num_vertices - 1) / 2) if num_vertices > 1 else 0

    return {
        "average_distance": average_distance,
        "diameter": diameter,
        "density": density,
        "num_edges": num_edges,
        "num_vertices": num_vertices
    }

def main():
    graph = read_graph_input()

    # Cálculo e exibição das métricas
    metrics = calculate_metrics(graph)
    if metrics:
        print(f"Distância Média: {metrics['average_distance']:.2f}")
        print(f"Diâmetro: {metrics['diameter']}")
        print(f"Densidade: {metrics['density']:.2f}")
        print(f"Tamanho (número de arestas): {metrics['num_edges']}")
        print(f"Ordem (número de vértices): {metrics['num_vertices']}")
    else:
        print("Grafo vazio.")

if __name__ == "__main__":
    main()
