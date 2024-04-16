#5-Fold
import numpy as np

arr = np.arange(0,6412) #INSTEAD OF 6412, WRITE THE NUMBER OF ANNOTATIONS IN TRAIN SET

np.random.shuffle(arr)

# Define the number of folds
num_folds = 5

# Calculate the size of each fold
fold_size = len(arr) // num_folds

# Split the arr into 5 folds
folds = np.array([arr[i * fold_size:(i + 1) * fold_size] for i in range(num_folds)])

# Print the first fold as an example
print("Fold 1:", folds.shape)

np.save("folds.npy", folds) #SAVE FOLDS