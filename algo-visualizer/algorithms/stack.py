NAME = "Stack"
TYPE = "structure"


def run(numbers):
    steps = []
    data = numbers.copy()

    for index in range(len(data) - 1, -1, -1):
        steps.append({
            "type": "compare",
            "index": index,
            "index1": index,
        })

    steps.append({
        "type": "finished",
        "array": data.copy(),
    })
    return steps
