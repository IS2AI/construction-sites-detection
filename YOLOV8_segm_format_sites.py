# convert polyYolo sites+footing anns to yolov8 segmentation format

map = {'1':'0',
       '19':'1',
       '20':'2',
       '21':'3',
       '22':'4',
       '23':'5'} 

with open("/raid/abylay_turekhassim/anns/fold_5_train.txt", 'r') as file: # PATH TO THE FILE WITH ANNOTATIONS IN POLY-YOLO FORMAT
    lines = file.readlines()

for line in lines:
    if len(line.split()) > 1:
        final_anns = ""
        split = line.split()
        name = split[0].split('/')[7][:-4] #ADJUST THE SPLIT SO THAT name = name of the file without .jpg

        for item in split[1:]:
            if item.split(',')[4] in ['1','19','20','21','22','23']:
                coords = item.split(',')[5:]
                for index in range(len(coords)):
                    coords[index] = str(float(coords[index])/600)
                final_anns += map.get(item.split(',')[4]) + ' ' + ' '.join(coords)
                if item != split[-1]:
                    final_anns += '\n'

        if final_anns != "" and final_anns[-1] == '\n':
            with open("/raid/abylay_turekhassim/v8_data/data/labels/fold5_train/"+name+'.txt', 'w') as write_file: #FOLDER WHERE TO STORE THE ANNOTATIONS
                write_file.write(final_anns[:-1])
        elif final_anns != "" and final_anns[-1] != '\n': 
            with open("/raid/abylay_turekhassim/v8_data/data/labels/fold5_train/"+name+'.txt', 'w') as write_file: #FOLDER WHERE TO STORE THE ANNOTATIONS
                write_file.write(final_anns)