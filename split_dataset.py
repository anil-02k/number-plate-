import os
import random
import shutil

# Set random seed for reproducibility
random.seed(42)

# Paths
images_dir = 'images'
labels_dir = 'labels'
output_dir = 'yolo_dataset'

# Split ratios
train_ratio = 0.8
val_ratio = 0.2
test_ratio = 0.0  # set to > 0 if you want a test set

# Create output structure
for split in ['train', 'val', 'test']:
    if split_ratio := (train_ratio if split == 'train' else val_ratio if split == 'val' else test_ratio):
        os.makedirs(os.path.join(output_dir, split, 'images'), exist_ok=True)
        os.makedirs(os.path.join(output_dir, split, 'labels'), exist_ok=True)

# Get all image files (we'll pair them with .txt files)
image_files = [f for f in os.listdir(images_dir) if f.endswith('.png')]

# Shuffle the list
random.shuffle(image_files)

# Split dataset
total = len(image_files)
train_end = int(total * train_ratio)
val_end = train_end + int(total * val_ratio)

train_files = image_files[:train_end]
val_files = image_files[train_end:val_end]
test_files = image_files[val_end:] if test_ratio > 0 else []

# Helper to copy files
def copy_files(file_list, split):
    for file in file_list:
        image_src = os.path.join(images_dir, file)
        label_src = os.path.join(labels_dir, os.path.splitext(file)[0] + '.txt')

        image_dst = os.path.join(output_dir, split, 'images', file)
        label_dst = os.path.join(output_dir, split, 'labels', os.path.splitext(file)[0] + '.txt')

        if os.path.exists(label_src):  # Only copy if label exists
            shutil.copyfile(image_src, image_dst)
            shutil.copyfile(label_src, label_dst)

# Copy files to each split
copy_files(train_files, 'train')
copy_files(val_files, 'val')
if test_ratio > 0:
    copy_files(test_files, 'test')

print(f"✅ Dataset split complete:\n- Train: {len(train_files)}\n- Val: {len(val_files)}\n- Test: {len(test_files)}")
