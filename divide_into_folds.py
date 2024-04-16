# CODE FOR DIVIDING THE ANNOTATION ACCORDING TO FOLDS
import numpy as np

folds = np.load('folds.npy')

with open('/raid/abylay_turekhassim/anns/new_cities_train.txt', 'r') as file: # PATH TO THE FILE WITH TRAIN ANNOTATIONS
    lines = file.readlines()

train = np.concatenate((folds[4],folds[0],folds[1],folds[2])) #SPECIFY THE FOLDS WHICH YOU WANT TO USE FOR TRAINING 
print(train.shape)

anns = ""
for index in train:
    anns += lines[index] 

with open('/raid/abylay_turekhassim/anns/fold_5_train.txt', 'w') as wfile: # PATH TO THE FILE WHERE YOU WANT TO STORE THE TRAIN ANNOTATIONS
    wfile.write(anns)

test = np.append(folds[3]) #SPECIFY THE FOLDS WHICH YOU WANT TO USE FOR TESTING
print(test.shape)

anns = ""
for index in test:
    anns += lines[index]

with open('/raid/abylay_turekhassim/anns/fold_5_test.txt', 'w') as wfile: # PATH TO THE FILE WHERE YOU WANT TO STORE THE TEST ANNOTATIONS
    wfile.write(anns)