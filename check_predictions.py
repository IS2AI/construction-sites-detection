import torch
from torchvision import ops
import cv2

predict_file = open("/raid/abylay_turekhassim/v8/predict.txt", 'r') # PATH TO THE FILE WITH PREDICTIONS
truth_file = open("/raid/abylay_turekhassim/anns/corrected_test.txt", 'r') # PATH TO THE FILE WTH GROUND TRUTH ANNOTATIONS FOR ALL CLASSES IN POLY-YOLO FORMAT
truth_lines = truth_file.readlines()
predict_lines = predict_file.readlines()

for line in predict_lines:
    if len(line.split()) > 1:
        img = line.split()[0]
        for info in truth_lines:
            if img in info:
                for item in line.split()[1:]:
                    pr_tl_x = float(item.split(',')[0])
                    pr_tl_y = float(item.split(',')[1])
                    pr_br_x = float(item.split(',')[2])
                    pr_br_y = float(item.split(',')[3])

                    max_iou = 0
                    for tr_item in info.split()[1:]:
                        #IF YOU WANT TO CHECK ONLY FOOTING PREDICTIONS, UNCOMMENT LINE BELOW
                        #if int(tr_item.split(',')[4]) not in [19,20,21,22,23]: 
                        tr_tl_x = float(tr_item.split(',')[0])
                        tr_tl_y = float(tr_item.split(',')[1])
                        tr_br_x = float(tr_item.split(',')[2])
                        tr_br_y = float(tr_item.split(',')[3])

                        ground_truth_bbox = torch.tensor([[tr_tl_x, tr_tl_y, tr_br_x, tr_br_y]], dtype=torch.float)
                        prediction_bbox = torch.tensor([[pr_tl_x, pr_tl_y, pr_br_x, pr_br_y]], dtype=torch.float)

                        # Get iou.
                        iou = ops.box_iou(ground_truth_bbox, prediction_bbox)
                        if iou.numpy()[0][0] > max_iou:
                            max_iou = iou.numpy()[0][0]

                    if max_iou < 0.1:
                        image = cv2.imread("/raid/abylay_turekhassim/v8_data/data/images/preds/" + img) # PATH TO THE FOLDER WITH IMAGES THAT WERE RUN THROUGH TRAINED MODEL 

                        top_left = (int(round(pr_tl_x)), int(round(pr_tl_y)))  # Replace x1 and y1 with your actual coordinates
                        bottom_right = (int(round(pr_br_x)), int(round(pr_br_y)))  # Replace x2 and y2 with your actual coordinates

                        # Draw the square on the image
                        color = (0, 0, 255)  # You can choose the color (BGR format)
                        thickness = 2  # You can adjust the thickness as needed
                        cv2.rectangle(image, top_left, bottom_right, color, thickness)
                        cv2.imwrite("/raid/abylay_turekhassim/v8_data/data/images/test/"+img, image) # PATH TO THE FOLDET WHERE YOU WANT TO STORE THE IMAGES FOR FURTHER CHECKING

truth_file.close()
predict_file.close()