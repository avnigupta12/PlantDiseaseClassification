import random
from scipy import ndarray
import skimage as sk

def random_rotation(image_array: ndarray):
    # pick a random degree of rotation between 25% on the left and 25% on the right
    random_degree = random.uniform(-25, 25)
    return sk.transform.rotate(image_array, random_degree)

def random_noise(image_array: ndarray):
    # add random noise to the image
    return sk.util.random_noise(image_array)

def horizontal_flip(image_array: ndarray):
    # horizontal flip doesn't need skimage, it's easy as flipping the image array of pixels !
    return image_array[:, ::-1]


import os                       # for working with files
import random
data_dir = r'D:\Concordia Study\COMP 6721-Capstone\Datasets\PlantDoc-Dataset'
folder_names = os.listdir(data_dir)

image_count_folders = {}
for disease in folder_names:
    image_count_folders[disease] = len(os.listdir(data_dir + '/' + disease))


max__image_count = 0
for folder_name in folder_names:
    if image_count_folders[folder_name] > max__image_count:
        max__image_count = image_count_folders[folder_name]


## LOGIC
for folder_name in folder_names:
    print(folder_name)
    num_files_desired = max__image_count - image_count_folders[folder_name] #50
    print("reading files")
    # loop on all files of the folder and build a list of files paths
    images = [os.path.join(os.path.join(data_dir, folder_name), f) for f in os.listdir(os.path.join(data_dir, folder_name)) if os.path.isfile(os.path.join(os.path.join(data_dir, folder_name), f))]
    print("files read")
    num_generated_files = 0
    while num_generated_files <= num_files_desired:
        # random image from the folder
        image_path = random.choice(images)
        # read image as an two dimensional array of pixels
        image_to_transform = sk.io.imread(image_path)
        
        
        # dictionary of the transformations functions we defined earlier
        available_transformations = {
            'rotate': random_rotation,
            'noise': random_noise,
            'horizontal_flip': horizontal_flip
        }

        # random num of transformations to apply
        num_transformations_to_apply = random.randint(1, len(available_transformations))

        num_transformations = 0
        transformed_image = None
        while num_transformations <= num_transformations_to_apply:
            # choose a random transformation to apply for a single image
            key = random.choice(list(available_transformations))
            transformed_image = available_transformations[key](image_to_transform)
            num_transformations += 1
            
            # define a name for our new file
            new_file_path = os.path.join(data_dir, folder_name, 'ag_' + str(num_generated_files)) + '.jpg'

        # write image to the disk
            sk.io.imsave(new_file_path, transformed_image)
            num_generated_files +=1
