NAME = "Graph Traversal"
TYPE = "graph"


def run(numbers):
    steps = []

    if not numbers:
        steps.append({
            "type": "finished",
            "array": [],
        })
        return steps

    graph = {
        index: [
            (index + 1) % len(numbers),
            (index + 2) % len(numbers),
        ]
        for index in range(len(numbers))
    }
    visited = set()
    stack = [0]

    while stack:
        node = stack.pop()
        if node in visited:
            continue

        visited.add(node)
        steps.append({
            "type": "compare",
            "index": node,
            "index1": node,
        })

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                stack.append(neighbor)

    steps.append({
        "type": "finished",
        "array": numbers.copy(),
    })

    return steps
