"""
copy images from D2S/images_org to D2S/images/split
"""
import os
import shutil
import json

data_path = "/home/thanh_nguyen/Datasets/MVTecD2S_v1"
data_path_save = "/home/thanh_nguyen/Datasets/MVTecD2S_v2"

# Specify image and annotation directories
img_dir = os.path.join(data_path, 'images')
ann_dir = os.path.join(data_path_save, 'r_annotations_v2')

splits = ['D2S_augmented', 'D2S_training_augmented', 'D2S_training', 'D2S_validation', 'D2S_test_info']

for split in splits:
    annFile = os.path.join(ann_dir, f'{split}.json')

    with open(annFile) as f:
        data = json.load(f)

    images = data['images']

    for img_dct in images:
        fname = img_dct['file_name'] 

        src = os.path.join(data_path, 'images', fname)

        output_path = os.path.join(data_path_save, 'images', split)

        if not os.path.exists(output_path):
            os.makedirs(output_path)
        dst = os.path.join(output_path, fname)
        shutil.copyfile(src, dst)





