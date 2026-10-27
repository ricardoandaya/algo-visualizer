NAME = "Selection Sort"
TYPE = "sort"


def run(numbers):
    steps = []
    data = numbers.copy()

    for first in range(len(data)):
        minimum_index = first

        for current in range(first + 1, len(data)):
            steps.append({
                "type": "compare",
                "index1": minimum_index,
                "index2": current,
            })

            if data[current] < data[minimum_index]:
                minimum_index = current

        if minimum_index != first:
            data[first], data[minimum_index] = (
                data[minimum_index],
                data[first],
            )
            steps.append({
                "type": "swap",
                "index1": first,
                "index2": minimum_index,
                "array": data.copy(),
            })

    steps.append({
        "type": "finished",
        "array": data.copy(),
    })

    return steps
