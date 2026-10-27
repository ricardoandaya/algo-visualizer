NAME = "Factorial"
TYPE = "math"


def run(numbers):
    steps = []

    if not numbers:
        steps.append({
            "type": "finished",
            "array": [],
        })
        return steps

    value = max(0, int(numbers[0]))
    result = 1

    for current in range(1, value + 1):
        steps.append({
            "type": "compare",
            "index1": current - 1,
            "index2": current,
        })
        result *= current

    steps.append({
        "type": "finished",
        "array": [result],
    })

    return steps
