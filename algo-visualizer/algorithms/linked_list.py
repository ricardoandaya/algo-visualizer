NAME = "Linked List"
TYPE = "structure"


def run(numbers):
    steps = []
    data = numbers.copy()

    for index, value in enumerate(data):
        steps.append({
            "type": "compare",
            "index": index,
            "index1": index,
        })
        data[index] = value

    steps.append({
        "type": "finished",
        "array": data.copy(),
    })
    return steps
