import argparse
from modules.settings import *
from modules.download import *

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Download data from cocodataset')
    parser.add_argument('--classes', nargs='+', type=str, required=True)
    args = vars(parser.parse_args())
    PrepareFolders()
    Download('annotations/instances_train2017.json',"train2017/", args['classes'])
    Download('annotations/instances_val2017.json', "val2017/", args['classes'])
    