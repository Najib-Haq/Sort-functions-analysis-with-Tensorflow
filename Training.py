import numpy as np
import csv
from sklearn.model_selection import train_test_split
import tensorflow as tf


def get_data(filename):
    data = []
    with open(filename,"r") as file:
        reader = csv.reader(file)
        i = 0
        for row in reader:
            if i%2 == 0: # because didnt use newline as row end in generating data file
                data.append(row)
            i += 1
    return data[1:]


def process_data(filename):
    data = get_data(filename)
    data = np.array(data, dtype = np.float32)
    #random.shuffle(data)
    sorted_data = []
    random_data = []
    reverse_data = []
    for row in data:
        if row[1] == 1:
            sorted_data.append(list(row[0:1])+list(row[4:]))
        elif row[2] == 1:
            random_data.append(list(row[0:1])+list(row[4:]))
        else:
            reverse_data.append(list(row[0:1])+list(row[4:]))
    sorted_data = np.array(sorted_data)
    random_data = np.array(random_data)
    reverse_data = np.array(reverse_data)
    return sorted_data, random_data, reverse_data


def print_data(a):
    for row in a:
        print(row)


def polynomial_regression_model(X, output_size):
    w_1 = tf.Variable(tf.zeros([output_size]))
    w_2 = tf.Variable(tf.zeros([output_size]))
    b = tf.Variable(tf.zeros([output_size]))

    term = tf.pow(X, 2)
    term = tf.add(tf.multiply(w_1, term), tf.multiply(w_2, X))
    y_model = tf.add(term, b)

    return y_model



def train_and_save_model(X_train,y_train,X_test,y_test,model_name,output_size = 6):
    print("For "+model_name)
    X = tf.placeholder(tf.float32)
    y = tf.placeholder(tf.float32, [output_size])

    y_model = polynomial_regression_model(X, output_size)
    cost = tf.reduce_mean(tf.square(y_model - y))
    train = tf.train.GradientDescentOptimizer(0.001).minimize(cost)

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        saver = tf.train.Saver()
        for i in range(2000):
            for (xt, yt) in zip(X_train, y_train):
                a = sess.run([cost, train], feed_dict={X: xt, y: yt})
            print("Epoch " + str(i) + "  : " + str(a))


        saver.save(sess,str(model_name+"/"+model_name+".ckpt"))

        overall_cost = 0
        for (xt, yt) in zip(X_test,y_test):
            pred = sess.run(y_model, feed_dict={X: xt})
            overall_cost += tf.reduce_mean(tf.square(pred - yt)).eval()
        print("Testing cost "+str(overall_cost/(len(X_test))))



def scale_data(data, max_data = 4000):
    return data/max_data



# def neural_net_model(X_data,input_dim):
#     W_1 = tf.Variable(tf.random_uniform([input_dim,6]))
#     b_1 = tf.Variable(tf.zeros([6]))
#     layer_1 = tf.add(tf.matmul(X_data,W_1), b_1)
#     layer_1 = tf.nn.relu(layer_1)
#     # layer 1 multiplying and adding bias then activation function
#     W_2 = tf.Variable(tf.random_uniform([6,32]))
#     b_2 = tf.Variable(tf.zeros([32]))
#     layer_2 = tf.add(tf.matmul(layer_1,W_2), b_2)
#     layer_2 = tf.nn.relu(layer_2)    # layer 2 multiplying and adding bias then activation function
#     W_O = tf.Variable(tf.random_uniform([32,6]))
#     b_O = tf.Variable(tf.zeros([6]))
#     output = tf.add(tf.matmul(layer_2,W_O), b_O)
#
#     return output

if __name__ == "__main__":
    sorted_data, random_data, reverse_data = process_data("data.csv")

    X_train = [0,0,0]
    X_test = [0,0,0]
    y_train = [0,0,0]
    y_test = [0,0,0]
    X_train[0], X_test[0], y_train[0], y_test[0] = train_test_split(sorted_data[:,0], sorted_data[:,1:-1], test_size=0.2)
    X_train[1], X_test[1], y_train[1], y_test[1] = train_test_split(random_data[:,0], random_data[:,1:-1], test_size=0.2)
    X_train[2], X_test[2], y_train[2], y_test[2] = train_test_split(reverse_data[:,0], reverse_data[:,1:-1], test_size=0.2)

    model_name = ["Sorted_data","Random_data","Reverse_data"]
    for i in range(len(X_train)):
        X_train[i] = scale_data(X_train[i])
        X_test[i] = scale_data(X_test[i])
        train_and_save_model(X_train[i], y_train[i], X_test[i], y_test[i], model_name[i])














