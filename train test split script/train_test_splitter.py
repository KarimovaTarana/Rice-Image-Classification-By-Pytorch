import os
import shutil
import random

# Define the paths
original_dataset_dir = '/Users/user/Downloads/archive (8)/Rice_Image_Dataset'
base_dir = '/Users/user/Desktop/Rice_project'  # This is where the new train/test directories will be created

# Create the base directories
train_dir = os.path.join(base_dir, 'train')
test_dir = os.path.join(base_dir, 'test')

os.makedirs(train_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

# Define the classes (assuming folder names are the rice types)
classes = ['Arborio', 'Basmati', 'Ipsala', 'Jasmine', 'Karacadag']

# Create class directories in train and test folders
for class_name in classes:
    os.makedirs(os.path.join(train_dir, class_name), exist_ok=True)
    os.makedirs(os.path.join(test_dir, class_name), exist_ok=True)

# Split the dataset
split_ratio = 0.8

for class_name in classes:
    class_dir = os.path.join(original_dataset_dir, class_name)
    images = os.listdir(class_dir)
    random.shuffle(images)
    
    split_point = int(len(images) * split_ratio)
    
    train_images = images[:split_point]
    test_images = images[split_point:]
    
    # Copy images to train directory
    for image in train_images:
        src = os.path.join(class_dir, image)
        dst = os.path.join(train_dir, class_name, image)
        shutil.copyfile(src, dst)
    
    # Copy images to test directory
    for image in test_images:
        src = os.path.join(class_dir, image)
        dst = os.path.join(test_dir, class_name, image)
        shutil.copyfile(src, dst)

print("Dataset split and organized successfully!")
