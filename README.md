# GOAL
To analyze the time complexity of some sorting functions with real time data and by using tensorflow, predict
the time complexity of these functions in other scenarios.

# Methodology
The sorting functions considered here are : Bubble sort, Selection sort, Insertion sort, Merge sort, Quick sort and Heap sort.
These functions are coded in ![sorting_algos](sorting_algos.py).
Configuration of the machine used in this project is : <br>
Processor : Intel(R) Core(TM) i5-8250U CPU @ 1.60GHz <br>
RAM : 8GB DDR4 <br>
Operating System : Windows 10 64-bit


### 1. Generating Data
Functions for generating data is in ![generate_data](generate_data.py). Here an array of a predetermined size is randomly generated and then 3 different cases are considered : already sorted data, randomly sorted data and reverse sorted data. For each size and for each case the same array is sorted using the aforementioned funcitons multiple times to get a more accurate representation of the time taken by the machine. Actually they were applied 100000/(length of array) times. The data is stored in file ![data.csv](data.csv).
Here array size started from 10 to 1000 in steps of 10, and 1000 to 4000 in steps of 100.

Restriction : During experimentation the program crashed after quick sort was applied on sorted data for array size > 4000 due to recursion limit set by the machine. That is why the upper limit of array size for this project was set to 4000.


### 2. Training
The functions are in ![Training](Training.py). Tensorflow was used in this regard. The method used was 2nd order polynomial regression. The thinking behind this selection is the time complexity of these sorting functions are at most O(n^2). That is why a 2nd order polynomial was used. The optimizer used here is the Gradient Descent Optimizer. A tensorflow model was created using this specification. The model has 1 input which will be the size of the array and 6 outputs representing the time taken in each sorting functions. <br>
This model was used for three different data cases : sorted_data, random_data and reversed_data.
As these three cases were independent, the training was done independently. Each model was trained using the generated data and for 2000 epochs each. The input data was scaled using the max array size as otherwise the optimization function would fail to optimize properly.<br>
The three models are saved in ![Sorted_data](Sorted_data) , ![Random_data](Random_data) and ![Reverse_data](Reverse_data) directories.


### 3. Data Collection from model
Using the models mentioned before, data was generated for array size 10 to 4000 and stored in ![output.csv](output.csv). The functions are in ![data_collection_from_model](data_collection_from_model.py). 

### 4. Analysis
Using the data generated and the data from training, different plots were created to get insight into the functions. This was done in ![analysis](analysis.py).

# Sort Functions Analysis
### Individual function performance
<img src="Images/Bubble sort.jpg" width="700"> <br>
From the plot, one can see that for both the three cases, this function has a 2nd order curve which is consistent as bubble sort has time complexity of O(n^2). The data generated from the model also seem to fit the training data. Also, even though all three cases are 2nd order, according to time taken : sorted_data < random_data < reverse_data.
<br><br>
<img src="Images/Selection sort.jpg" width="700"> <br>
Here also, all three cases bear a 2nd order curve. Selection sort also has time complexity of O(n^2) for all three cases and thus this is consistent. Here too sorted_data < random_data < reverse_data but the difference in their time is more negligible.
<br><br>
<img src="Images/Insertion sort.jpg" width="700"> <br>
Here random_data and reverse_data have 2nd order curves while sorted_data seems linear. Insertion sort has time complexity of O(n) for sorted data and O(n^2) for all other cases. Thus this is consistent. Also, sorted_data < random_data < reverse_data is also observed.
<br><br>
<img src="Images/Merge sort.jpg" width="700"> <br>
Here all three cases show a curve which is not 2nd order and also not quite linear. This actually represents the time complexity of O(nlogn) of Merge Sort. Also sorted_data < reverse_data < random_data is observed even though the difference is quite negligible. Furthermore, the data used for training seems to fluctuate a lot which might have contributed to this representation.
<br><br>
<img src="Images/Quick sort.jpg" width="700"> <br>
Here sorted_data and reverse_data shows a 2nd order curve whereas random_data shows what appears to be linear characteristic, but this is because the other data is takes a much longer time resulting in a increases y axis limit. Thus this can be construed as O(nlogn) characteristic which is consistent with the time complexities of quick sort. The Worst Case for quick sort is O(n^2) and the best case is O(nlogn); worst case appears for sorted or reverse_sorted data. Also random_data < reverse_data < sorted_data is observed from the plot.
<br><br>
<img src="Images/Heap sort.jpg" width="700"> <br>
Like Merge sort, all three cases show a linear logarithmic characteristic. This is consistent with Heap sort's time complexity of O(nlogn) for all three cases. Like Merge sort, the data used for training seems to fluctuate a lot. Here random_data < reverse_data < sorted_data is observed even though the difference is quite negligible. But this might be because of the fluctuating training data.













