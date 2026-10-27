NAME = "Insertion Sort"
TYPE = "sort"


def run(numbers):
    steps = []
    data = numbers.copy()

    for index in range(1, len(data)):
        current = index

        while current > 0:
            steps.append({
                "type": "compare",
                "index1": current - 1,
                "index2": current,
            })

            if data[current - 1] <= data[current]:
                break

            data[current - 1], data[current] = (
                data[current],
                data[current - 1],
            )
            steps.append({
                "type": "swap",
                "index1": current - 1,
                "index2": current,
                "array": data.copy(),
            })
            current -= 1

    steps.append({
        "type": "finished",
        "array": data.copy(),
    })

    return steps