"""
copy images from D2S/images_org to D2S/images/split
"""
import os
import shutil
import json

data_path = "/Users/thanhnguyen/Documents/Datasets/MVTec/D2S"

# Specify image and annotation directories
img_dir = os.path.join(data_path, 'images_org')
ann_dir = os.path.join(data_path, 'annotations_org')

splits = ['D2S_validation', 'D2S_test_info']

for split in splits:
    annFile = os.path.join(ann_dir, f'{split}.json')

    with open(annFile) as f:
        data = json.load(f)

    images = data['images']

    for img_dct in images:
        fname = img_dct['file_name'] 

        src = os.path.join(data_path, 'images_org', fname)

        output_path = os.path.join(data_path, 'images', split)

        if not os.path.exists(output_path):
            os.makedirs(output_path)
        dst = os.path.join(output_path, fname)
        shutil.copyfile(src, dst)





