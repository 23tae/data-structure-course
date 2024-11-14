from timeit import default_timer as timer
from random import sample
import pandas as pd
import matplotlib.pyplot as plt


def generate_numbers(size=10000):
    return sample(range(0, size), size)


# Selection Sort
def selection_sort(data):
    n = len(data)
    for i in range(n-1):
        least = i
        for j in range(i+1, n):
            if (data[j] < data[least]):
                least = j
        data[i], data[least] = data[least], data[i]


# Insertion Sort
def insertion_sort(data):
    n = len(data)
    for i in range(1, n):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key


# Bubble Sort
def bubble_sort(data):
    n = len(data)
    for i in range(n-1, 0, -1):
        b_changed = False
        for j in range(i):
            if (data[j] > data[j + 1]):
                data[j], data[j+1] = data[j+1], data[j]
                b_changed = True
        if not b_changed:
            break


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


# 정렬, 표 생성
results = []
for i in range(10000, 100001, 10000):
    data = generate_numbers(i)
    sorts = {
        'Selection': selection_sort,
        'Insertion': insertion_sort,
        'Bubble': bubble_sort,
        'Quick': quick_sort
    }
    row = {'size': i}
    for name, sort_func in sorts.items():
        temp = data[:]
        start = timer()
        sort_func(temp)
        end = timer()
        row[name] = (end-start)
    results.append(row)
df = pd.DataFrame(results)

# 그래프 시각화
plt.figure(figsize=(10, 6))
plt.plot(df['size'], df['Selection'], label='Selection Sort', marker='o')
plt.plot(df['size'], df['Insertion'], label='Insertion Sort', marker='s')
plt.plot(df['size'], df['Bubble'], label='Bubble Sort', marker='^')
plt.plot(df['size'], df['Quick'], label='Quick Sort', marker='d')
plt.title('Sorting Algorithms Performance Comparison')
plt.xlabel('Size', loc='right')
plt.ylabel('Time (sec)', loc='top')
plt.legend()
plt.show()
