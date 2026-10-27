NAME = "Binary Tree"
TYPE = "structure"


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(root, value, steps):
    if root is None:
        return Node(value)

    steps.append({
        "type": "compare",
        "index": value % 10,
        "index1": value % 10,
    })

    if value < root.value:
        root.left = insert(root.left, value, steps)
    else:
        root.right = insert(root.right, value, steps)

    return root


def run(numbers):
    steps = []
    root = None

    for value in numbers:
        root = insert(root, value, steps)

    steps.append({
        "type": "finished",
        "array": numbers.copy(),
    })
    return steps
