NAME = "Bubble Sort"
TYPE = "sort"


def run(numbers):
    steps = []
    data = numbers.copy()

    for end in range(len(data) - 1, 0, -1):
        swapped = False

        for current in range(end):
            steps.append({
                "type": "compare",
                "index1": current,
                "index2": current + 1,
            })

            if data[current] > data[current + 1]:
                data[current], data[current + 1] = (
                    data[current + 1],
                    data[current],
                )
                steps.append({
                    "type": "swap",
                    "index1": current,
                    "index2": current + 1,
                    "array": data.copy(),
                })
                swapped = True

        if not swapped:
            break

    steps.append({
        "type": "finished",
        "array": data.copy(),
    })

    return steps
