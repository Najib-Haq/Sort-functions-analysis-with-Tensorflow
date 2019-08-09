import analysis as a
import numpy as np
import generate_data as gd
import data_collection_from_model as dcfm
import sorting_algos as s
import sys

def get_accuracy(filename_data, filename_training_data):
    data = a.get_data(filename_data)
    data = np.array(data, dtype=np.float32)

    training_data = a.get_data(filename_training_data, True)
    training_data = np.array(training_data[1:], dtype=np.float32)

    indexes = a.get_minsort_index(data[:,4:])
    print(len(indexes))
    accuracy = 0
    j = 117  # starting from 400
    for i in range(1170, len(indexes)):
        if data[i][0] == training_data[j][0]:
            if indexes[i] == training_data[j][-1]:
                accuracy += 1
            j += 1
    return accuracy/(j-117)



if __name__ == "__main__":

    # print("Overall accuracy is "+str(get_accuracy("output.csv","data.csv")))
    arr = []
    data = []
    model_name = ["Sorted_data","Random_data","Reverse_data"]
    model_data = []
    functions = [s.bubble_sort, s.selection_sort, s.insertion_sort, s.merge_sort, s.quick_sort, s.heap_sort]
    sortings = ["Bubble","Selection","Insertion","Merge","Quick","Heap"]

    for i in range(3):
        model_data.append(dcfm.restore_model(model_name[i]))

    sys.setrecursionlimit(100000)

    while True:
        print("1. Generate array.")
        print("2. Bubble Sort\t3. Selection Sort\t4. Insertion Sort\t")
        print("5. Merge Sort\t6. Quick Sort\t7. Heap Sort\t")
        print("8. Recommended Sort\t9. Exit")
        print("Enter your choice : ")
        n = int(input())
        if n==1:
            arr = []
            print("Enter size :")
            size = int(input())
            print("1. Enter your own.\t2. Generate Array Automatically")
            choice = int(input())
            if choice == 1:
                for i in range(size):
                    arr.append(int(input()))
            else:
                gd.gen_array(arr,size)
            print("1. Sorted\t2. Random\t3. Reverse")
            choice = int(input())
            sorted = False
            if choice == 1:
                arr.sort()
                sorted = True
            elif choice == 3:
                arr.sort(reverse=True)
            data = dcfm.get_y(size,model_data[choice-1])
        elif n == 2:
            print("Time taken for Bubble sort on array size of "+str(size)+" is : "+str(gd.get_time(arr,sorted,[functions[n-2]])[0]))
            print("Time taken from model : "+str(data[n-2]))
        elif n == 3:
            print("Time taken for Selection sort on array size of "+str(size)+" is : "+str(gd.get_time(arr,sorted,[functions[n-2]])[0]))
            print("Time taken from model : "+str(data[n-2]))
        elif n == 4:
            print("Time taken for Insertion sort on array size of "+str(size)+" is : "+str(gd.get_time(arr,sorted,[functions[n-2]])[0]))
            print("Time taken from model : "+str(data[n-2]))
        elif n == 5:
            print("Time taken for Merge sort on array size of "+str(size)+" is : "+str(gd.get_time(arr,sorted,[functions[n-2]])[0]))
            print("Time taken from model : "+str(data[n-2]))
        elif n == 6:
            print("Time taken for Quick sort on array size of "+str(size)+" is : "+str(gd.get_time(arr,sorted,[functions[n-2]])[0]))
            print("Time taken from model : "+str(data[n-2]))
        elif n == 7:
            print("Time taken for Heap sort on array size of "+str(size)+" is : "+str(gd.get_time(arr,sorted,[functions[n-2]])[0]))
            print("Time taken from model : "+str(data[n-2]))
        elif n == 8:
            for i in range(6):
                print(sortings[i],end='\t')
            print('\n')
            for i in range(6):
                print(data[i],end='\t')
            print('\n')
            get_time = gd.get_time(arr,sorted,functions)
            for i in range(6):
                print(format(get_time[i], '.8f'),end='\t')
            print('\n')
            print("Recommended : ")
            print("From model : "+str(sortings[int(a.get_minsort_index([data])[0])]))
            print("From device : "+str(sortings[int(a.get_minsort_index([get_time])[0])]))

        elif n == 9:
            break
        print("\n\n")


    sys.setrecursionlimit(1000)
