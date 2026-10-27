NAME = "Fibonacci Sequence"
TYPE = "math"


def run(numbers):
    steps = []

    if not numbers:
        steps.append({
            "type": "finished",
            "array": [],
        })
        return steps

    length = max(0, int(numbers[0]))
    sequence = [0]

    if length >= 1:
        sequence = [0, 1]

    for index in range(2, length + 1):
        steps.append({
            "type": "compare",
            "index1": index - 1,
            "index2": index - 2,
        })
        sequence.append(sequence[-1] + sequence[-2])

    steps.append({
        "type": "finished",
        "array": sequence[:length + 1],
    })

    return steps
