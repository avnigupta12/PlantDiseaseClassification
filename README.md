# Group A: Early Identification and Classification of Plant Disease Using CNN Models

## Goal of the Project:

    The present era is characterized by famines and climatic changes, hence plant disease identification and classification have become a necessity. Disease identification by domain experts is time-consuming and costly and cannot be used on a global scale. Due to this, early identification and classification of plant disease is an important research area.

    This study uses three datasets that are distinct in size, number of classes and captured in different environmental conditions. Both Training from Scratch and Transfer Learning are explored. Three CNN models, VGG16, ResNet50, and AlexNet are trained on the three datasets. Due to the variety of challenges in different datasets, image pre-processing techniques such as online and offline data augmentation and image normalization have been used.

    The study aims to compare the performance by using metrics like time, loss and accuracy plots. Evaluation parameters used for comparison are Accuracy, Precision, Sensitivity Recall, and F1 score.

---

## System Requirements

### Hardware

- GPU - 4 GB or more
- RAM / Memory - 8 GB or more
- Additional Storage - 4 GB for the Datasets + 10 GB working storage

### Software

- Python - 3.7-3.9 (limitations of PyTorch)
- pip
- PyTorch and torchvision
- Jupyter Notebook or any other compatible notebook platform
- git

### Python Libraries Required

pip can be used to install the latest version of the below libraries.

- torch and torchvision (Note: Ignore if already installed already in previous step, preferred)
- torchsummary
- numpy
- pandas
- matplotlib
- PIL
- sklearn

<u>Hint:</u> Best environment is Kaggle or Google Colab. They already has all the libraries required. The ones that are not installed already are installed in the first cell of all notebooks.

---

## How to Download and use the Dataset

### Dataset Source:

| Dataset Name  | Dataset after Offline Augmentation                                             | Original Dataset                                                  |
| ------------- | ------------------------------------------------------------------------------ | ----------------------------------------------------------------- |
| Plant Village | [Link: Kaggle](https://www.kaggle.com/datasets/anantshukla1/plantvillagecolor) | [Link: Mendeley](https://data.mendeley.com/datasets/t6j2h22jpx/2) |
| Plantaek      | [Link: Kaggle](https://www.kaggle.com/datasets/anantshukla1/plantaek6721)      | [Link: GitHub](https://github.com/spMohanty/PlantVillage-Dataset) |
| PlantDoc      | [Link: Kaggle](https://www.kaggle.com/datasets/anantshukla1/plantdoc6721)      | [Link: GitHub](https://github.com/pratikkayal/PlantDoc-Dataset)   |

### How to use Dataset

Use the 'Dataset after Offline Augmentation' link to download the Datasets from Kaggle. The datasets are available publicly and hence no permissions are needed to access them.

Once downloaded, you can use the path of the Dataset and assign it to the variable 'data_dir' present in the 4th cell of the Notebook.

---

## Instruction on how to train/validate your model

- Download the appropriate notebook from GitHub
- Download the Dataset
- Import the Dataset by using the path of the dataset directory and assigning it to the variable 'data_dir' in the 4th cell of the Notebook.
- Run all the cells using the 'Run all' command
- This would first import the dataset, then train the model, and then finally validate the CNN model along with the visualization that contain the accuracy and loss curves, confusion matix, t-SNE and other plots.

---

## Instructions on how to run the pre-trained model on the provided sample test dataset

There are two types of transfer learning techniques fine tuning and deep tuning (feature extraction). In this project we performed deep tuning which is known as feature extraction. Feature extraction begins with a pretrained model and then it only updates the final layer weights from which it can derive the predictions. This is because of the usage the pretrained CNN models as a fixed feature-extractor and can only change to the output layer.

Here, all the network weights are frozen except the final layer and set to (requires_grad = False) to freeze the parameters so that the gradients are not computed in (backward ()).

- Initialize the pretrained model
- Reshape the final layers to have the same number of outputs as the number of classes in the dataset
- Define optimization algorithm which parameters to update during training
- Finally, run the training loop
