import tensorflow as tf
import csv

MAX_INPUT_SIZE = 4000

def restore_model(model_name,output_size = 6):
    w_1 = tf.Variable(tf.zeros([output_size]))
    w_2 = tf.Variable(tf.zeros([output_size]))
    b = tf.Variable(tf.zeros([output_size]))

    print("For " + model_name)
    with tf.Session() as sess:
        saver = tf.train.Saver()
        saver.restore(sess, str(model_name+"/"+model_name+".ckpt"))
        coeffs = [w_1.eval(), w_2.eval(), b.eval()]

    return coeffs


def get_y(X, coeffs):
    X = X/MAX_INPUT_SIZE
    return coeffs[0]*(X**2) + coeffs[1]*X + coeffs[2]


def get_data(max_x = MAX_INPUT_SIZE):
    data = []
    model_name = ["Sorted_data","Random_data","Reverse_data"]
    model_data = []
    for i in range(len(model_name)):
        model_data.append(restore_model(model_name[i]))

    for n in range(10,max_x+1):
        for order in range(3):
            row_data = [n]
            if order == 0:
                row_data += [1,0,0]
            elif order == 1:
                row_data += [0,1,0]
            else:
                row_data += [0,0,1]
            row_data += list(get_y(n, model_data[order]))
            data.append(row_data)
    return data


def write_to_csv(filename, data):
    with open(filename,"w+",newline='') as file:
        writer = csv.writer(file,dialect=csv.excel)
        writer.writerows(data)




if __name__ == "__main__":
    data = get_data()
    write_to_csv("output.csv",data)
















