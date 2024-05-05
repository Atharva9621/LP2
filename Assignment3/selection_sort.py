from typing import List

def selection_sort(arr: List)->None:
    for i in range(len(arr)):
        min_elem = i+arr[i:].index(min(arr[i:]))
        arr[i], arr[min_elem] = arr[min_elem], arr[i]

if __name__=="__main__":
    arr = [1,4,2,7,9,6,8,3,5,2]
    print("Before Sorting : ", arr)
    selection_sort(arr)
    print("After Selection sort : ", arr)