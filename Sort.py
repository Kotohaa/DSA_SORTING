import os
import time

#-------------------------------QUICKSORT--------------------------------

def Quicksort(arr, left, right):
    # Chọn pivot (phần tử mốc) ở giữa mảng
    mark = arr[(left + right) // 2]
    i = left
    j = right

    while i <= j:
        # Tìm phần tử bên trái >= pivot
        while arr[i] < mark:
            i += 1

        # Tìm phần tử bên phải <= pivot
        while arr[j] > mark:
            j -= 1

        # Nếu i chưa vượt j thì đổi chỗ hai phần tử
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    # Đệ quy sắp xếp nửa bên trái
    if left < j:
        Quicksort(arr, left, j)

    # Đệ quy sắp xếp nửa bên phải
    if i < right:
        Quicksort(arr, i, right)

    return arr

#-------------------------------HEAPSORT--------------------------------

def heapify(arr, n, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2

    # nếu con trái lớn hơn gốc
    if left < n and arr[left] > arr[largest]:
        largest = left

    # nếu con phải lớn hơn lớn nhất hiện tại
    if right < n and arr[right] > arr[largest]:
        largest = right

    # nếu gốc không phải lớn nhất
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapsort(arr):
    n = len(arr)

    # xây max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # trích từng phần tử ra khỏi heap
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr

#-------------------------------MERGESORT--------------------------------

def merge(left, right):
    result = []
    i = j = 0

    # so sánh từng phần tử
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # thêm phần còn lại
    result.extend(left[i:])
    result.extend(right[j:])

    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # chia mảng
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # trộn hai mảng đã sắp xếp
    return merge(left, right)

#-------------------------------XULY--------------------------------

def benchmark_one_file(filepath):
    with open(filepath, "r") as f:
        data = list(map(float, f.read().split()))

    print(f"\n File: {os.path.basename(filepath)}")

    # QuickSort
    arr_qs = data.copy()
    start = time.perf_counter()
    Quicksort(arr_qs, 0, len(arr_qs) - 1)
    print(f"QuickSort: {time.perf_counter() - start:.6f} giây")

    # HeapSort
    arr_hs = data.copy()
    start = time.perf_counter()
    heapsort(arr_hs)
    print(f"HeapSort:  {time.perf_counter() - start:.6f} giây")

    # MergeSort
    arr_ms = data.copy()
    start = time.perf_counter()
    arr_ms = merge_sort(arr_ms)
    print(f"MergeSort: {time.perf_counter() - start:.6f} giây")

    # Python sort
    arr_py = data.copy()
    start = time.perf_counter()
    arr_py = sorted(arr_py)
    print(f"Python sort: {time.perf_counter() - start:.6f} giây")


def main():
    data_folder = "data"

    files = sorted(
        f for f in os.listdir(data_folder)
        if f.startswith("data") and f.endswith(".txt")
    )

    for filename in files:
        filepath = os.path.join(data_folder, filename)
        benchmark_one_file(filepath)

if __name__ == "__main__":
    main()

