import cv2
import os

def split_image(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Calculate the dimensions for the smaller images
    height, width, _ = image.shape
    small_width = small_height = 600
    
    gap = 600 #distance between the small images
    limit = 1200 #at which point stop splitting

    # Verify if the image size is valid for splitting
    if width % small_width != 0 or height % small_height != 0:
        print("Invalid image size for splitting.")
        return

    # Create a list to store the smaller images
    small_images = []

    # Split the image into smaller images
    for i in range(0, limit, gap):
        for j in range(0, limit, gap):
            small_image = image[j:j+small_height, i:i+small_width]
            small_images.append(small_image)

    # Save the smaller images
    for i, small_image in enumerate(small_images):
        cv2.imwrite(r"D:\archive\new_all_600x600_with_anns\\"+image_path.split('\\')[-1][:-4] + f"_{i}.jpg", small_image)

    print("Image splitting completed!")
