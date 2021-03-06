#! python3
# quickSort.py-快速排序

import random


# 快速排序核心函数
def quickSortCore(arr, left, right):
    # 1. 定阈值
    cutOff = 8
    if right - left >= cutOff:
        # 2. 选主元
        pivot = medium3(arr, left, right)
        l = left + 1
        r = right - 2
        # 3. 快排
        while True:
            while arr[l] < pivot:
                l += 1
            while arr[r] > pivot:
                r -= 1
            if arr[l] < arr[r]:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1
            else:
                break;
        arr[l], arr[right - 1] = arr[right - 1], arr[l]
        quickSortCore(arr, left, l - 1)
        quickSortCore(arr, l + 1, right)
    else:
        insertSort(arr, left, right)
    return arr


# 插入排序
def insertSort(arr, left, right):
    for i in range(left + 1, right + 1):
        temp = arr[i]
        j = i
        while j > 0 and arr[j-1] > temp:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = temp
    return arr


# 选主元
def medium3(arr, left, right):
    center = (left + right) // 2
    if arr[left] > arr[center]:
        arr[left], arr[center] = arr[center], arr[left]
    if arr[center] > arr[right]:
        arr[center], arr[right] = arr[right], arr[center]
    if arr[left] > arr[center]:
        arr[left], arr[center] = arr[center], arr[left]
    arr[center], arr[right-1] = arr[right-1], arr[center]
    return arr[right-1]


# 统一接口
def quickSort(arr):
    return quickSortCore(arr, 0, len(arr) - 1)


# 测试
<<<<<<< HEAD
N = 30
arr = [random.randint(0, N * 10) for _ in range(N)]
=======
N = 10
arr = [random.randint(-N, N) for _ in range(N)]
print(arr)
>>>>>>> 94953b659577795277bf9084b4fa798007eb82d9
arr = quickSort(arr)
# print('finish')
print(arr)
