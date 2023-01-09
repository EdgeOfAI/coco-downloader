import json
import cv2
import os
import matplotlib.pyplot as plot
import shutil
from tqdm import tqdm


def Download(annotation_file, input_path, selected_classes):
    
    output_path = "coco_dataset/"
    file_names = os.listdir(input_path)


    #getting ids of classes as categories -> set
    categories = dict()
    lines = open('classes.txt', 'r').readlines()
    class_ids = dict()
    for line in lines:
        class_name =  line.split()[0]
        if len(line.split()) == 3:
            class_name += ' ' + line.split()[1]
        class_id = int(line.split()[-1])
        class_ids[class_name] = class_id
    
    class_name = ''
    count = 0
    file_object = open('coco_dataset/classes.txt', 'a')
    for word in selected_classes:
        if class_name == '':
            class_name = word
        else:
            class_name += ' ' + word
        if not class_name in class_ids and len(class_name.split()) > 1:
            raise NameError(f"No such class found:{class_name}")
        elif class_name in class_ids:
            categories[class_ids[class_name]] = count 
            count += 1
            file_object.write(class_name + '\n')
            class_name = ''
    if class_name != '':
        raise NameError(f"No such class found:{class_name}")
    

    #Loading json files
    f = open(annotation_file)
    data = json.load(f)
    f.close()

    
    #extract image annotation from json data
    def get_img_ann(image_id):
        img_ann = []
        isFound = False
        for ann in data['annotations']:
            if ann['image_id'] == image_id and ann['category_id'] in categories :
                img_ann.append(ann)
                isFound = True
        if isFound:
            return img_ann
        else:
            return None


    #check if image is exist in json data
    def get_img(filename):
        for img in data['images']:
            if img['file_name'] == filename:
                return img

    
    for img in tqdm(data['images']):
        filename = img['file_name']
        img_id = img['id']
        img_w = img['width']
        img_h = img['height']

        # Get Annotations for this image
        img_ann = get_img_ann(img_id)

        if img_ann:
            # Opening file for current image
            file_object = open(f"{output_path}labels/{filename.split('.')[0]}.txt", "a")

            ##copy images

            source = os.path.join(input_path,filename)
            destination = f"{output_path}images/{filename}"

            try:
                shutil.copy(source, destination)
                # print("File copied successfully.")
            # If source and destination are same
            except shutil.SameFileError:
                # print("Source and destination represents the same file.")
                continue

            # file_names.append(filename)




            for ann in img_ann:
                current_category = categories[ann['category_id']] # As yolo format labels start from 0 
                current_bbox = ann['bbox']
                x = current_bbox[0]
                y = current_bbox[1]
                w = current_bbox[2]
                h = current_bbox[3]
                
                # Finding midpoints
                x_centre = (x + (x+w))/2
                y_centre = (y + (y+h))/2
                
                # Normalization
                x_centre = x_centre / img_w
                y_centre = y_centre / img_h
                w = w / img_w
                h = h / img_h
                
                # Limiting upto fix number of decimal places
                x_centre = format(x_centre, '.6f')
                y_centre = format(y_centre, '.6f')
                w = format(w, '.6f')
                h = format(h, '.6f')
                    
                # Writing current object 
                
                file_object.write(f"{current_category} {x_centre} {y_centre} {w} {h}\n")

            file_object.close()
