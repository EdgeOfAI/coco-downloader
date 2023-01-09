import os
import shutil
from tqdm import tqdm
import requests, zipfile, io



def PrepareFolders():

    #Annonation Files
    if os.path.isdir('annotations'):
        print("Annotation files are already downloaded ✅")
    else:
        
        print("Downloading annonation files")
        #downloading annotation
        r = requests.get("https://images.cocodataset.org/annotations/annotations_trainval2017.zip", verify=False)
        z = zipfile.ZipFile(io.BytesIO(r.content))
        z.extractall("./")

    #Train images
    if os.path.isdir('train2017'):
        print('Train images are already downloaded ✅')
    else:
        cmd = input("Train images are 18GB, do you want to continue?  (yes/no) :")
        if cmd != '':
            if cmd[0].lower() == 'n':
                exit(0);
        print("Downloading train images ")
        r = requests.get("http://images.cocodataset.org/zips/train2017.zip", verify=False)
        z = zipfile.ZipFile(io.BytesIO(r.content))
        z.extractall("./")

    #Val images
    if os.path.isdir('val2017'):
        print('Validation images are already downloaded ✅')
    else:
        cmd = input("Validation images are 1GB, do you want to continue?  (yes/no) :")
        if cmd != '':
            if cmd[0].lower() == 'n':
                exit(0);
        print("Downloading validation images")
        r = requests.get("http://images.cocodataset.org/zips/val2017.zip", verify=False)
        z = zipfile.ZipFile(io.BytesIO(r.content))
        z.extractall("./")




    #destination folders
    if os.path.isdir('coco_dataset'):
        text =  input("Old dataset folders found, do you remove them to download new dataset?  (yes/no) :")
        if text != '':
            if text[0].lower == 'n':
                exit(0);
        shutil.rmtree('coco_dataset')
    os.mkdir('coco_dataset')
    os.mkdir('coco_dataset/images')
    os.mkdir('coco_dataset/labels')