NAME = "Linear Search"
TYPE = "search"


def run(numbers, target):
    steps = []

    for index, value in enumerate(numbers):
        steps.append({
            "type": "compare",
            "index": index,
        })

        if value == target:
            steps.append({
                "type": "found",
                "index": index,
                "array": numbers.copy(),
            })
            return steps

    steps.append({
        "type": "not_found",
        "array": numbers.copy(),
    })
    return steps
