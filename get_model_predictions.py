from ultralytics import YOLO
import os
from PIL import Image

#os.environ["CUDA_VISIBLE_DEVICES"] = '11,12,13,14'

model = YOLO('/raid/abylay_turekhassim/runs/segment/sites/weights/best.pt')  # PATH TO THE TRAINED MODEL

full_text = ""
for img in os.listdir('/raid/abylay_turekhassim/v8_data/data/images/segm_test'): # PATH OT THE FOLDER WITH IMAGES FOR PREDICTION


    results = model('/raid/abylay_turekhassim/v8_data/data/images/segm_test/' + img)  # PATH OT THE FOLDER WITH IMAGES FOR PREDICTION

    # Show the results
    full_text += img
    for r in results:
        for box in r.boxes.xyxy.cpu().numpy():
            full_text += " " + ",".join([str(x) for x in box.tolist()])
        im_array = r.plot(boxes=True, labels=True)  # YOU CAN DELETE boxes=True, labels=True if you do not need boxes and labels for predicted objects
        im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
        im.save('/raid/abylay_turekhassim/v8_data/data/images/preds/' + img)  # PATH TO THE FOLDER WHERE TO STORE THE PREDICTIONS

    full_text += '\n'

with open("/raid/abylay_turekhassim/v8/predict.txt", "w") as file: # PATH TO THE FILE WHERE TO STORE THE PREDICTIONS
    file.write(full_text)
