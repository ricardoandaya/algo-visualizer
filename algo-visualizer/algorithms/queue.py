NAME = "Queue"
TYPE = "structure"


def run(numbers):
    steps = []
    data = numbers.copy()
    queue = list(data)

    for index in range(len(queue)):
        steps.append({
            "type": "compare",
            "index": index,
            "index1": index,
        })

    steps.append({
        "type": "finished",
        "array": queue.copy(),
    })
    return steps
