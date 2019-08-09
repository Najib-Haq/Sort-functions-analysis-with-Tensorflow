import time
import random
import sys


#-------------------------------BUBBLE SORT--------------------------------------------#
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]



#-------------------------------SELECTION SORT--------------------------------------------#
def selection_sort(arr):
    for i in range(len(arr)-1):
        idx = i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[idx]:
                idx = j
        arr[i],arr[idx] = arr[idx],arr[i]



#-------------------------------INSERTION SORT--------------------------------------------#
def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while (j>=0 and arr[j]>key):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key




#-------------------------------MERGE SORT--------------------------------------------#
def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    l_arr = []
    r_arr = []

    for i in range(n1):
        l_arr.append(arr[left + i])
    for j in range(n2):
        r_arr.append(arr[mid + 1 + j])

    i,j,k = 0,0,left
    while (i<n1 and j<n2):
        if l_arr[i] <= r_arr[j]:
            arr[k] = l_arr[i]
            i+=1
        else:
            arr[k] = r_arr[j]
            j+=1
        k+=1

    while (i<n1):
        arr[k] = l_arr[i]
        i+=1
        k+=1

    while (j < n2):
        arr[k] = r_arr[j]
        j+=1
        k+=1



def merge_sort_utility(arr, left, right):
    if left<right:
        mid = left + (right-left)//2
        merge_sort_utility(arr, left, mid)
        merge_sort_utility(arr, mid+1, right)

        merge(arr, left, mid, right)



def merge_sort(arr):
    merge_sort_utility(arr, 0, len(arr)-1)




#-------------------------------QUICK SORT--------------------------------------------#
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j]<=pivot:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1


def quick_sort_utility(arr,low,high):
    if low<high:
        partition_index = partition(arr,low, high)
        quick_sort_utility(arr,low,partition_index-1)
        quick_sort_utility(arr, partition_index+1, high)


def quick_sort(arr):
    quick_sort_utility(arr,0,len(arr)-1)




#-------------------------------HEAP SORT--------------------------------------------#
def heapify(arr, n, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2
    if(left<n and arr[left]>arr[largest]):
        largest = left
    if(right<n and arr[right]>arr[largest]):
        largest = right
    if(largest != i):
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)



def heap_sort(arr):
    n = len(arr)
    for i in range((n//2)-1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)





if __name__ == "__main__":
    sys.setrecursionlimit(10000000)
    time_taken = 0
    l = []
    for i in range(4000):
        l.append(random.randrange(0,1000000000))
    l.sort()


    for i in range(100000//4000):
        al = l.copy()
        start_time = time.time()
        quick_sort(al)
        time_taken += time.time()-start_time

    print("Time taken is "+str(time_taken/(100000//4000))+" seconds")
    print(al)
    sys.setrecursionlimit(1000)






















