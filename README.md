
# <div align="center">COCO Downloader ToolKit</div>
Download dataset for custom classes from [COCO Dataset](https://cocodataset.org/#home)

## <div align="center">Documentation</div>

### Installation
Clone repo and install [requirements.txt](https://github.com/EdgeOfAI/coco-downloader/blob/main/requirements.txt) in a
[**Python>=3.9.0**](https://www.python.org/) environment

```bash
git clone https://github.com/EdgeOfAI/coco-downloader.git  # clone
cd coco-downloader
pip3 install -r requirements.txt  # install
```
Download and unzip [Train images](http://images.cocodataset.org/zips/train2017.zip) in coco-downloader folder

Download and unzip [Validation images](http://images.cocodataset.org/zips/val2017.zip) in coco-downloader folder

The two files will be downloaded automatically by toolkit, but due to their large size(19GB at all), it is strongly recommended that you copy them if you have these files locally.



<details>
    <summary> Directory structure after downloading/copying train and val images </summary>

```
main_folder
│   main.py
│
└───train2017
|     |    0fdea8a716155a8e.jpg
|     |    2fe4f21e409f0a56.jpg
|     |    ...
|    
└───val2017
      |    1sdea8a71615554e.jpg
      |    3s541f21e409ffdg6.jpg
      |    ...
```  


</details>

###   Download Custom Dataset


Choose class names from [Available classes](https://github.com/EdgeOfAI/coco-downloader/blob/main/classes.txt) and provide choosen class names to the required argument

Required argument:
  - classes


Run main.py to download dataset for custom classes
```bash
python3 main.py --classes car person # downloads dataset for Car and Person classes with default parameters
```

The algorithm will take care to download all the necessary files and build the directory structure like this:
```
main_folder
│   main.py
│
└───coco_dataset
    │   classes.txt
    │
    └───images
    |    │   0fdea8a716155a8e.jpg
    |    │   2fe4f21e409f0a56.jpg
    |    |   ...
    |
    └───labels
        |    0fdea8a716155a8e.txt
        |    2fe4f21e409f0a56.txt
        |    ...
```  
