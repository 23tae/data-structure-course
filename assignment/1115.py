from timeit import default_timer as timer
from random import sample


def generate_numbers(size=10000):
    return sample(range(0, size * 3), size)


# Quick Sort
def quick_sort(data, left=0, right=None):
    if right is None:
        right = len(data) - 1
    if left < right:
        q = partition(data, left, right)
        quick_sort(data, left, q-1)
        quick_sort(data, q+1, right)


def partition(data, left, right):
    low = left + 1
    high = right
    pivot = data[left]

    while low <= high:
        while low <= right and data[low] < pivot:
            low += 1
        while high >= left and data[high] > pivot:
            high -= 1
        if low < high:
            data[low], data[high] = data[high], data[low]
    data[left], data[high] = data[high], data[left]
    return high


# Merge Sort
def merge_sort(data, left=0, right=None):
    if right is None:
        right = len(data) - 1
    if left < right:
        mid = (left + right) // 2
        merge_sort(data, left, mid)
        merge_sort(data, mid + 1, right)
        merge(data, left, mid, right)


def merge(data, left, mid, right):
    temp = []
    i = left
    j = mid + 1

    while i <= mid and j <= right:
        if data[i] <= data[j]:
            temp.append(data[i])
            i += 1
        else:
            temp.append(data[j])
            j += 1
    while i <= mid:
        temp.append(data[i])
        i += 1
    while j <= right:
        temp.append(data[j])
        j += 1
    for i in range(len(temp)):
        data[left + i] = temp[i]


# Binary Search
def binary_search(data, find_data):
    start = 0
    end = len(data) - 1

    while (start <= end):
        mid = (start + end) // 2
        if find_data == data[mid]:
            return mid
        elif find_data > data[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return -1


# Interpolation Search
def interpolation_search(data, target):
    low = 0
    high = len(data) - 1

    while low <= high and target >= data[low] and target <= data[high]:
        if low == high:
            if data[low] == target:
                return low
            return -1
        pos = low + ((target - data[low]) * (high - low) //
                     (data[high] - data[low]))
        if data[pos] == target:
            return pos
        if data[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1


if __name__ == "__main__":
    data1 = generate_numbers(1000000)
    data2 = generate_numbers(1000000)

    find_data = int(input("\n찾으려는 수를 입력하세요: "))

    quick_sort(data1)
    merge_sort(data2)

    start = timer()
    pos1 = binary_search(data1, find_data)
    end = timer()
    print(f"\nBinary Search:\ntime: {(end - start):.6f} seconds")
    if pos1 == -1:
        print(f"number {find_data} not found.")
    else:
        print(f"position of {find_data}: {pos1}")

    start = timer()
    pos2 = interpolation_search(data2, find_data)
    end = timer()
    print(f"\nInterpolation Search:\ntime: {(end - start):.6f} seconds")
    if pos2 == -1:
        print(f"number {find_data} not found.")
    else:
        print(f"position of {find_data}: {pos2}")
