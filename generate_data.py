import sorting_algos as s
import random
import time
import csv
import sys

INT_MAX = 10000000
MAX_ITERATION = 100000
sort_functions = [s.bubble_sort, s.selection_sort, s.insertion_sort, s.merge_sort, s.quick_sort, s.heap_sort]

def gen_array(arr, size):
    for i in range(size):
        arr.append(random.randrange(0,INT_MAX))


def get_time(arr, sorted, func_list = sort_functions):
    ans_list = []
    for func in func_list:
        # print(func)
        time_taken = 0
        copy_arr = arr.copy()
        for i in range(MAX_ITERATION//len(arr)):
            if sorted == False:
                copy_arr = arr.copy()
            start_time = time.time()
            func(copy_arr)
            time_taken += (time.time() - start_time)
        ans_list.append(time_taken/(MAX_ITERATION//len(arr)))
    ans_list.append(ans_list.index(min(ans_list)))
    return ans_list


def get_data(start_size, end_size):
    # headers = ["Size","Sorted","Random","Reverse","Bubble","Selection","Insertion","Merge","Quick","Heap","Best"]
    # total_data = [headers]
    total_data = []
    for size in range(start_size, end_size+1, 100):
        print("Generating for array size "+str(size))
        for case in range(3):
            arr = []
            data = [size]
            gen_array(arr, size)
            print("case is " + str(case))
            if case == 0:
                sorted = True
                data += [1,0,0] #signifies whether sorted or reverse sorted or random
                arr.sort()
            else:
                sorted = False
                if case == 1: # random
                    data += [0,1,0]
                else:
                    data += [0,0,1] # reverse sorted
                    arr.sort(reverse=True)
            data += get_time(arr, sorted)
            total_data.append(data)
    return total_data



def write_to_csv(filename, data):
    with open(filename,"a",newline='') as file:
        writer = csv.writer(file,dialect=csv.excel)
        writer.writerows(data)




if __name__ == "__main__":
    random.seed(time.time())
    sys.setrecursionlimit(1000000)
    total_data = get_data(1300,4000)
    write_to_csv("data.csv", total_data)  #DOESNT WORK FOR BEST CASE QUICK SORT WHEN ARR_SIZE > 4000
    sys.setrecursionlimit(1000)