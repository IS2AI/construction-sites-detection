# CREATE ANNOTATION IN POLY-YOLO COMPATIBLE FORMAT

import xml.etree.ElementTree as ET
import os
##################
def calculate_intersection_y(polygon_vertices, intersection_y):
    intersection_points = []

    for i in range(len(polygon_vertices)):
        x1, y1 = polygon_vertices[i]
        x2, y2 = polygon_vertices[(i + 1) % len(polygon_vertices)]

        if (y1 > intersection_y and y2 < intersection_y) or (y1 < intersection_y and y2 > intersection_y):
            if x1 != x2:  # Check for non-vertical edge
                # Calculate slope and y-intercept of the line segment
                m = (y2 - y1) / (x2 - x1)
                b = y1 - m * x1

                # Calculate x-coordinate of the intersection point
                intersection_x = (intersection_y - b) / m
                intersection_points.append((intersection_x, intersection_y))
            else:  # Handle vertical edge
                intersection_x = x1
                intersection_points.append((intersection_x, intersection_y))

    return intersection_points

#########################
def calculate_intersection_x(polygon_vertices, intersection_x):
    intersection_points = []

    for i in range(len(polygon_vertices)):
        x1, y1 = polygon_vertices[i]
        x2, y2 = polygon_vertices[(i + 1) % len(polygon_vertices)]

        if (x1 > intersection_x and x2 < intersection_x) or (x1 < intersection_x and x2 > intersection_x):
            if x1 != x2:  # Check for non-vertical edge
                # Calculate slope and y-intercept of the line segment
                m = (y2 - y1) / (x2 - x1)
                b = y1 - m * x1

                # Calculate y-coordinate of the intersection point
                intersection_y = m * intersection_x + b
                intersection_points.append((intersection_x, intersection_y))
            else:  # Handle vertical edge
                intersection_y = y1
                intersection_points.append((intersection_x, intersection_y))

    return intersection_points

#####################
def extract_polygon_points(xml_file):
    # Parse the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    classes = {"excavation": "0",
               "footing":"1",
               "crane":"2",
               "machinery":"3",
               "road":"4",
               "mat.piles":"5",
               "cdw.piles":"6",
               "alt.en.piles":"7",
               "office":"8",
               "storage":"9",
               "work.fac":"10",
               "entry":"11",
               "parking":"12",
               "fabrication":"13",
               "waste facility":"14",
               "bin":"15",
               "fence":"16",
               "water management":"17",
               "scaffolding":"18",
               "site.1":"19",
               "site.2":"20",
               "site.3":"21",
               "site.4":"22",
               "site.5":"23"}


    # Find lines with <polygon> tags
    polygon_lines = root.find('image').findall('polygon')
    # HERE SHOULD BE THE PATH TO THE FOLDER WITH ALL THE IMAGES
    out_line = r"D:\archive\new_all_600x600_with_anns\\" + xml_file.split('\\')[-2] + '_0' + '.jpg'
    # Extract text within the 'points' label for each line
    vertices = []
    for line in polygon_lines:
        up_left=[]
        
        points_text = line.attrib['points']
        coords = points_text.split(';')
        
        for item in coords:
            x=item.split(',')[0]
            y=item.split(',')[1]
            vertices.append((float(x),float(y)))
            if float(x)<=600 and float(y)<=600:
                up_left.append(x+','+y)

        x_intersection = calculate_intersection_x(vertices, 600)
        y_intersection = calculate_intersection_y(vertices, 600)
        
        x_center = False
        y_center = False
        if len(x_intersection) != 0:
            for xy in x_intersection:
                if xy[0]<=600 and xy[1]<=600:
                    up_left.append(str(xy[0])+","+str(xy[1]))
                    x_center = True

        if len(y_intersection) != 0:
            for xy in y_intersection:
                if xy[0]<=600 and xy[1]<=600:
                    up_left.append(str(xy[0])+","+str(xy[1]))
                    y_center = True
        
        if x_center == True and y_center == True:
            up_left.append("600,600")
        vertices.clear()
        if len(up_left) != 0:
            ints=[]
            ux = 0
            lx = 10000
            bx = 10000
            rx = 0
            for coords in up_left:
                left = float(coords.split(',')[0])
                right = float(coords.split(',')[1])
                ints.append(str(left))
                ints.append(str(right))
                
                if left < lx:
                    lx = left
                if right < bx:
                    bx = right
                if right > ux:
                    ux = right
                if left > rx:
                    rx = left
            try:
                out_line += " " + str(lx) + "," + str(bx) + "," + str(rx) + "," + str(ux) + "," + classes.get(line.attrib ['label']) + "," + ",".join(ints).strip() 
            except:
                continue    
    # HERE SHOULD BE THE PATH TO THE FOLDER WITH ALL THE IMAGES
    if out_line != r"D:\archive\new_all_600x600_with_anns\\" + xml_file.split('\\')[-2] + '_0' + '.jpg':
        file = r"D:\archive\data\data\FINAL_FULL_ANNOTATIONS_600.txt" # PATH TO THE FILE WHERE YOU WANT TO STORE THE ANNOTATIONS
        file = open(file, "a")
        file.write(out_line + '\n')
        file.close()


    # HERE SHOULD BE THE PATH TO THE FOLDER WITH ALL THE IMAGES
    out_line = r"D:\archive\new_all_600x600_with_anns\\" + xml_file.split('\\')[-2] + '_1' + '.jpg'
    # Extract text within the 'points' label for each line
    for line in polygon_lines:
        dn_left=[]
        
        points_text = line.attrib['points']
        coords = points_text.split(';')
        
        for item in coords:
            x=item.split(',')[0]
            y=item.split(',')[1]
            vertices.append((float(x),float(y)))
            if float(x)<=600 and float(y)>=600:
                dn_left.append(x+','+y)
                
        x_intersection = calculate_intersection_x(vertices, 600)
        y_intersection = calculate_intersection_y(vertices, 600)
        
        x_center = False
        y_center = False
        if len(x_intersection) != 0:
            for xy in x_intersection:
                if xy[0]<=600 and xy[1]>=600:
                    dn_left.append(str(xy[0])+","+str(xy[1]))
                    x_center = True
        
        if len(y_intersection) != 0:
            for xy in y_intersection:
                if xy[0]<=600 and xy[1]>=600:
                    dn_left.append(str(xy[0])+","+str(xy[1]))
                    y_center = True

        if x_center == True and y_center == True:
            dn_left.append("600,600")
        vertices.clear()
        if len(dn_left) != 0:
            ints=[]
            ux = 0
            lx = 10000
            bx = 10000
            rx = 0
            for coords in dn_left:
                left = float(coords.split(',')[0])
                right = float(coords.split(',')[1])-600
                ints.append(str(left))
                ints.append(str(right))
                
                if left < lx:
                    lx = left
                if right < bx:
                    bx = right
                if right > ux:
                    ux = right
                if left > rx:
                    rx = left
            try:
                out_line += " " + str(lx) + "," + str(bx) + "," + str(rx) + "," + str(ux) + "," + classes.get(line.attrib ['label']) + "," + ",".join(ints).strip() 
            except:
                continue               
    # HERE SHOULD BE THE PATH TO THE FOLDER WITH ALL THE IMAGES    
    if out_line != r"D:\archive\new_all_600x600_with_anns\\" + xml_file.split('\\')[-2] + '_1' + '.jpg':
        file = r"D:\archive\data\data\FINAL_FULL_ANNOTATIONS_600.txt" # PATH TO THE FILE WHERE YOU WANT TO STORE THE ANNOTATIONS
        file = open(file, "a")
        file.write(out_line + '\n')
        file.close()      

    # HERE SHOULD BE THE PATH TO THE FOLDER WITH ALL THE IMAGES
    out_line = r"D:\archive\new_all_600x600_with_anns\\" + xml_file.split('\\')[-2] + '_2' + '.jpg'
    # Extract text within the 'points' label for each line
    for line in polygon_lines:
        up_right=[]
        
        points_text = line.attrib['points']
        coords = points_text.split(';')
        
        for item in coords:
            x=item.split(',')[0]
            y=item.split(',')[1]
            vertices.append((float(x),float(y)))
            if float(x)>=600 and float(y)<=600:
                up_right.append(x+','+y)

        x_intersection = calculate_intersection_x(vertices, 600)
        y_intersection = calculate_intersection_y(vertices, 600)

        x_center = False
        y_center = False
        if len(x_intersection) != 0:
            for xy in x_intersection:
                if xy[0]>=600 and xy[1]<=600:
                    up_right.append(str(xy[0])+","+str(xy[1]))
                    x_center = True
        if len(y_intersection) != 0:
            for xy in y_intersection:
                if xy[0]>=600 and xy[1]<=600:
                    up_right.append(str(xy[0])+","+str(xy[1]))
                    y_center = True
                    
        if x_center == True and y_center == True:
            up_right.append("600,600")
        vertices.clear()
        if len(up_right) != 0:
            ints=[]
            ux = 0
            lx = 10000
            bx = 10000
            rx = 0
            for coords in up_right:                
                left = float(coords.split(',')[0])-600
                right = float(coords.split(',')[1])
                ints.append(str(left))
                ints.append(str(right))
                
                if left < lx:
                    lx = left
                if right < bx:
                    bx = right
                if right > ux:
                    ux = right
                if left > rx:
                    rx = left
            try:
                out_line += " " + str(lx) + "," + str(bx) + "," + str(rx) + "," + str(ux) + "," + classes.get(line.attrib ['label']) + "," + ",".join(ints).strip() 
            except:
                continue 
    # HERE SHOULD BE THE PATH TO THE FOLDER WITH ALL THE IMAGES
    if out_line != r"D:\archive\new_all_600x600_with_anns\\" + xml_file.split('\\')[-2] + '_2' + '.jpg':
        file = r"D:\archive\data\data\FINAL_FULL_ANNOTATIONS_600.txt" # PATH TO THE FILE WHERE YOU WANT TO STORE THE ANNOTATIONS
        file = open(file, "a")
        file.write(out_line + '\n')
        file.close()
    
    # HERE SHOULD BE THE PATH TO THE FOLDER WITH ALL THE IMAGES
    out_line = r"D:\archive\new_all_600x600_with_anns\\" + xml_file.split('\\')[-2] + '_3' + '.jpg'
    # Extract text within the 'points' label for each line
    for line in polygon_lines:
        dn_right=[]
        
        points_text = line.attrib['points']
        coords = points_text.split(';')
        
        for item in coords:
            x=item.split(',')[0]
            y=item.split(',')[1]
            vertices.append((float(x),float(y)))
            if float(x)>=600 and float(y)>=600:
                dn_right.append(x+','+y)
        
        x_intersection = calculate_intersection_x(vertices, 600)
        y_intersection = calculate_intersection_y(vertices, 600)

        x_center = False
        y_center = False
        if len(x_intersection) != 0:
            for xy in x_intersection:
                if xy[0]>=600 and xy[1]>=600:
                    dn_right.append(str(xy[0])+","+str(xy[1])) 
                    x_center = True
                    
        if len(y_intersection) != 0:
            for xy in y_intersection:
                if xy[0]>=600 and xy[1]>=600:
                    dn_right.append(str(xy[0])+","+str(xy[1]))
                    y_center = True
        
        if x_center == True and y_center == True:
            dn_right.append("600,600")        
        vertices.clear()
        if len(dn_right) != 0:
            ints=[]
            ux = 0
            lx = 10000
            bx = 10000
            rx = 0
            for coords in dn_right:
                left = float(coords.split(',')[0])-600
                right = float(coords.split(',')[1])-600
                ints.append(str(left))
                ints.append(str(right))
                
                if left < lx:
                    lx = left
                if right < bx:
                    bx = right
                if right > ux:
                    ux = right
                if left > rx:
                    rx = left
            try:
                out_line += " " + str(lx) + "," + str(bx) + "," + str(rx) + "," + str(ux) + "," + classes.get(line.attrib ['label']) + "," + ",".join(ints).strip() 
            except:
                continue  
    # HERE SHOULD BE THE PATH TO THE FOLDER WITH ALL THE IMAGES
    if out_line != r"D:\archive\new_all_600x600_with_anns\\" + xml_file.split('\\')[-2] + '_3' + '.jpg':
        file = r"D:\archive\data\data\FINAL_FULL_ANNOTATIONS_600.txt" # PATH TO THE FILE WHERE YOU WANT TO STORE THE ANNOTATIONS
        file = open(file, "a")
        file.write(out_line + '\n')
        file.close()      

def traverse_folders(path):
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path):
            extract_polygon_points(item_path)
        elif os.path.isdir(item_path):
            print("Entering folder:", item_path)
            traverse_folders(item_path)
                
                

starting_path = r"C:\Users\DELL\Desktop\cities" # FOLDER WHERE YOU STORE THE ANNOTATION FROM CVAT
traverse_folders(starting_path)

