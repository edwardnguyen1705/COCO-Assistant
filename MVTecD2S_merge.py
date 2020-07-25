"""
merge subsets (set1 and set2) into a merged set.

Expected Directory Structure
.
├── images
│   ├── set1
│   ├── set2
|   |── ...

|
├── annotations
│   ├── set1.json
│   ├── set2.json
|   |── ...

"""
import os

from coco_assistant import COCO_Assistant

data_path = "/Users/thanhnguyen/Documents/Datasets/MVTec/D2S"

# Specify image and annotation directories
img_dir = os.path.join(data_path, 'images')
ann_dir = os.path.join(data_path, 'annotations')

# Create COCO_Assistant object
cas = COCO_Assistant(img_dir, ann_dir)
cas.merge(merge_images=True)




