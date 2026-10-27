NAME = "Quick Sort"
TYPE = "sort"


def run(numbers):
    steps = []
    data = numbers.copy()

    def partition(low, high):
        pivot_value = data[high]
        smaller_index = low - 1

        for current in range(low, high):
            steps.append({
                "type": "compare",
                "index1": current,
                "index2": high,
                "pivot": high,
            })

            if data[current] <= pivot_value:
                smaller_index += 1
                if smaller_index != current:
                    data[smaller_index], data[current] = (
                        data[current],
                        data[smaller_index],
                    )
                    steps.append({
                        "type": "swap",
                        "index1": smaller_index,
                        "index2": current,
                        "array": data.copy(),
                    })

        smaller_index += 1
        if smaller_index != high:
            data[smaller_index], data[high] = (
                data[high],
                data[smaller_index],
            )
            steps.append({
                "type": "swap",
                "index1": smaller_index,
                "index2": high,
                "array": data.copy(),
            })

        return smaller_index

    def quick_sort(low, high):
        if low >= high:
            return

        pivot_index = partition(low, high)
        quick_sort(low, pivot_index - 1)
        quick_sort(pivot_index + 1, high)

    if len(data) > 1:
        quick_sort(0, len(data) - 1)

    steps.append({
        "type": "finished",
        "array": data.copy(),
    })

    return steps
