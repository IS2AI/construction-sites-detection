import shutil
import os

# Write the path to the file with annotations. The images from that file will be transferred to the new folder
# Note that the beginning of each line in this file should begin with the path to the folder where you store all the images
with open("/raid/abylay_turekhassim/anns/corrected_test.txt", 'r') as file:
    # Read all lines at once and store them in a list
    lines = file.readlines()

# Iterate over the lines and print them
for line in lines:
    img_name = line.strip().split(' ')[0]

    # Specify the destination folder path
    destination_folder = "/raid/abylay_turekhassim/v8_data/data/images/segm_test" # Path to the folder where you want to store the images

    # Construct the destination file path by joining the destination folder path and the source file name
    destination_file = os.path.join(destination_folder, os.path.basename(img_name))

    # Move the file, if the file was not found, it will be printed
    try:
        shutil.move(img_name, destination_file)
    except:
        print(img_name)