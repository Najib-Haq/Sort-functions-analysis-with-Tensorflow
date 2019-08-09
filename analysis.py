import matplotlib.pyplot as plt
import csv
import numpy as np

def get_data(filename, case = False):
    data = []
    with open(filename,"r") as file:
        reader = csv.reader(file)
        i = 0
        for row in reader:
            i += 1
            if case == True and i%2 == 0: # because didnt use newline as row end in generating data file
                continue
            data.append(row)
    return data


def plot_individual_sortings(data, training_data, sorting):

    plt.figure(figsize=(16, 10))
    plt.grid(color='grey', linewidth=0.8, alpha=0.4)
    sorted_data = [data[i] for i in range(0,len(data),3)]
    random_data = [data[i] for i in range(1,len(data),3)]
    reverse_data = [data[i] for i in range(2,len(data),3)]
    # print(str(len(sorted_data)+len(random_data)+len(reverse_data)))


    x_data= range(10,4001)
    x_training_data = list(range(10,1001,10))+list(range(1100,4001,100))
    sorted_training_data = []
    random_training_data = []
    reverse_training_data = []
    for i in range(len(x_training_data)):
        sorted_training_data.append(training_data[3*i])
        random_training_data.append(training_data[(3 * i)+1])
        reverse_training_data.append(training_data[(3 * i)+2])


    plt.plot(x_data, sorted_data, label = "sorted data", color = 'g')
    plt.plot(x_data, random_data, label="random data", color = 'b')
    plt.plot(x_data, reverse_data, label="reverse data", color = 'purple')
    plt.plot(x_training_data, sorted_training_data, label = "sorted training data", marker = ".", color = 'springgreen')
    plt.plot(x_training_data, random_training_data, label = "random training data", marker = ".", color = 'deepskyblue')
    plt.plot(x_training_data, reverse_training_data, label = "reverse training data", marker = ".", color = 'fuchsia')
    plt.legend(loc = "best")
    plt.xlabel("Input Array Size ")
    plt.ylabel("Time (seconds)")
    plt.title(str("For "+sorting+" sort"))
    plt.savefig(str("Images/"+sorting+" sort.jpg"),bbox_inches='tight')
    plt.show()



def plot_individual_cases(data, training_data):
    sorted_data = np.array([data[i] for i in range(0, len(data), 3)])
    random_data = np.array([data[i] for i in range(1, len(data), 3)])
    reverse_data = np.array([data[i] for i in range(2, len(data), 3)])
    # print(str(len(sorted_data)+len(random_data)+len(reverse_data)))
    all_data = [sorted_data, random_data, reverse_data]
    x_data = range(10, 4001)
    x_training_data = list(range(10, 1001, 10)) + list(range(1100, 4001, 100))
    sorted_training_data = []
    random_training_data = []
    reverse_training_data = []
    for i in range(len(x_training_data)):
        sorted_training_data.append(training_data[3 * i])
        random_training_data.append(training_data[(3 * i) + 1])
        reverse_training_data.append(training_data[(3 * i) + 2])

    sorted_training_data = np.array(sorted_training_data)
    random_training_data = np.array(random_training_data)
    reverse_training_data = np.array(reverse_training_data)
    all_data += [sorted_training_data, random_training_data, reverse_training_data]
    sortings = ["Bubble", "Selection", "Insertion", "Merge", "Quick", "Heap"]
    colors = ["crimson","magenta","dodgerblue","seagreen","cyan","gold"]
    cases = ["Sorted","Random","Reverse"]



    for case in range(len(cases)):
        plt.figure(figsize=(16,10))
        plt.grid(color='grey', linewidth=0.8, alpha=0.4)
        for i in range(len(sortings)):
            plt.plot(x_data, all_data[case][:,4+i], label = str(sortings[i]+" sort"), color = colors[i])
        plt.legend(loc="best")
        plt.xlabel("Input Array Size ")
        plt.ylabel("Time (seconds)")
        plt.title(str("For " + cases[case] + " data"))
        plt.savefig(str("Images/" + cases[case] + " data(Data from model).jpg"), bbox_inches='tight')
        plt.show()

    for case in range(len(cases)):
        plt.figure(figsize=(16,10))
        plt.grid(color='grey', linewidth=0.8, alpha=0.4)
        for i in range(len(sortings)):
            plt.plot(x_training_data, all_data[case+3][:,4+i], label = str(sortings[i]+" sort"), color = colors[i])
        plt.legend(loc="best")
        plt.xlabel("Input Array Size ")
        plt.ylabel("Time (seconds)")
        plt.title(str("For " + cases[case] + " data"))
        plt.savefig(str("Images/" + cases[case] + " data(Training data).jpg"), bbox_inches='tight')
        plt.show()



def plot_usage(data_index, training_data_index):
    sorted_data = [data_index[i] for i in range(0, len(data_index), 3)]
    random_data = [data_index[i] for i in range(1, len(data_index), 3)]
    reverse_data = [data_index[i] for i in range(2, len(data_index), 3)]
    # print(str(len(sorted_data)+len(random_data)+len(reverse_data)))
    all_data = [sorted_data, random_data, reverse_data]
    x_data = range(10, 4001)
    x_training_data = list(range(10, 1001, 10)) + list(range(1100, 4001, 100))
    sorted_training_data = []
    random_training_data = []
    reverse_training_data = []
    for i in range(len(x_training_data)):
        sorted_training_data.append(training_data_index[3 * i])
        random_training_data.append(training_data_index[(3 * i) + 1])
        reverse_training_data.append(training_data_index[(3 * i) + 2])
    all_data += [sorted_training_data, random_training_data, reverse_training_data]
    data = ["data","training data"]
    sortings = ["Bubble", "Selection", "Insertion", "Merge", "Quick", "Heap"]
    colors = ["crimson", "magenta", "dodgerblue", "seagreen", "cyan", "gold"]
    cases = ["Sorted", "Random", "Reverse"]
    x = [x_data,x_training_data]



    for i in range(len(data)):
        set_index = set([])
        length = 0
        plt.figure(figsize=(16, 10))
        plt.grid(color='grey', linewidth=0.8, alpha=0.4)
        plt.gca().yaxis.axes.grid(False)
        plt.gca().xaxis.axes.grid(True)
        for case in range(len(cases)):
            print("case : ",case)
            if i==0:
                start = 400
            else:
                start = 100
            for x_index in range(start,len(all_data[(3*i)+case])):
                set_index.add(all_data[(3*i)+case][x_index])
                if length!=len(set_index):
                    plt.plot([x[i][x_index], x[i][x_index]], [case, case + 1],
                             color=colors[int(all_data[(3 * i) + case][x_index])],
                             label=sortings[int(all_data[(3*i)+case][x_index])])
                    length += 1
                else:
                    plt.plot([x[i][x_index], x[i][x_index]], [case, case + 1],
                             color=colors[int(all_data[(3 * i) + case][x_index])])

        plt.yticks(np.arange(0,3.1,0.5), ("-","-","Sorted","-","Random","-","Reverse"))
        plt.legend(loc="upper right")
        plt.xlabel("Input Array Size ")
        plt.ylabel("Sortings")
        plt.title(str("From " + data[i]))
        plt.savefig(str("Images/" + data[i]+".jpg"), bbox_inches='tight')
        plt.show()




def get_minsort_index(data):
    index = []
    for row in data:
        index.append(int(np.where(row == np.min(row))[0]))
    return index




if __name__ == "__main__":
    data = get_data("output.csv")
    data = np.array(data, dtype=np.float32)

    training_data = get_data("data.csv", True)
    training_data = np.array(training_data[1:], dtype=np.float32)

    sortings = ["Bubble","Selection","Insertion","Merge","Quick","Heap"]
    # for i in range(len(sortings)):
    #     plot_individual_sortings(data[:,4+i], training_data[:,4+i], sortings[i])
    #
    # plot_individual_cases(data, training_data)
    indexes = get_minsort_index(data[:,4:])
    plot_usage(indexes, training_data[:,-1])
