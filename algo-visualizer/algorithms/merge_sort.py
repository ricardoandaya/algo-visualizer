NAME = "Merge Sort"
TYPE = "sort"


def run(numbers):
    steps = []
    data = numbers.copy()

    def merge(left, middle, right):
        left_values = data[left:middle + 1]
        right_values = data[middle + 1:right + 1]

        left_index = 0
        right_index = 0
        merged_index = left

        while left_index < len(left_values) and right_index < len(right_values):
            steps.append({
                "type": "compare",
                "index1": left + left_index,
                "index2": middle + 1 + right_index,
            })

            if left_values[left_index] <= right_values[right_index]:
                data[merged_index] = left_values[left_index]
                left_index += 1
            else:
                data[merged_index] = right_values[right_index]
                right_index += 1

            merged_index += 1

        while left_index < len(left_values):
            data[merged_index] = left_values[left_index]
            left_index += 1
            merged_index += 1

        while right_index < len(right_values):
            data[merged_index] = right_values[right_index]
            right_index += 1
            merged_index += 1

    def merge_sort(left, right):
        if left >= right:
            return

        middle = (left + right) // 2
        merge_sort(left, middle)
        merge_sort(middle + 1, right)
        merge(left, middle, right)

    if len(data) > 1:
        merge_sort(0, len(data) - 1)

    steps.append({
        "type": "finished",
        "array": data.copy(),
    })

    return steps
