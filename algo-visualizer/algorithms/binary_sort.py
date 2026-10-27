NAME = "Binary Search"
TYPE = "search"


def run(numbers, target):
    steps = []
    data = sorted(numbers)
    left = 0
    right = len(data) - 1

    while left <= right:
        middle = (left + right) // 2
        steps.append({
            "type": "compare",
            "index": middle,
            "pivot": middle,
        })

        if data[middle] == target:
            steps.append({
                "type": "found",
                "index": middle,
                "array": data.copy(),
            })
            return steps

        if data[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    steps.append({
        "type": "not_found",
        "array": data.copy(),
    })
    return steps
