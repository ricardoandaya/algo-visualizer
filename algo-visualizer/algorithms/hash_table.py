NAME = "Hash Table"
TYPE = "structure"


def run(numbers):
    steps = []

    if not numbers:
        steps.append({
            "type": "finished",
            "array": [],
        })
        return steps

    size = max(5, len(numbers))
    table = [[] for _ in range(size)]

    for value in numbers:
        bucket = value % size
        steps.append({
            "type": "compare",
            "index": bucket,
            "index1": bucket,
        })
        table[bucket].append(value)

    steps.append({
        "type": "finished",
        "array": numbers.copy(),
    })

    return steps
