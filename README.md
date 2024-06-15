# Rice Image Classification By PyTorch

## Project Description
This project aims to classify different types of rice grains using a convolutional neural network implemented in PyTorch.

## Dataset
Due to size limitations, the dataset used in this project is not included in this repository. You can download the dataset from Kaggle:
- [Rice Image Dataset on Kaggle]([https://www.kaggle.com/yourusername/rice-image-dataset](https://www.kaggle.com/datasets/muratkokludataset/rice-image-dataset))

After downloading, place the dataset files in the `data/` directory of this repository.

## Installation Instructions
1. Clone the repository:
    ```sh
    git clone https://github.com/KarimovaTarana/Rice-Image-Classification-By-Pytorch.git
    cd Rice-Image-Classification-By-Pytorch
    ```

2. Install the required packages:
    ```sh
    pip install torch torchvision numpy pandas jupyter scikit-learn matplotlib
    ```

## Usage
1. Ensure the dataset is properly placed in the `data/` directory.
2. Split the dataset into training and testing sets:
    ```sh
    python scripts/split_data.py
    ```

3. Run the Jupyter Notebook to train and evaluate the model:
    ```sh
    jupyter notebook notebooks/rice_classification.ipynb
    ```

## Project Structure
- `data/`: Placeholder for the dataset files (not included in this repository).
- `notebooks/`: Jupyter Notebook for model training and evaluation.
- `scripts/`: Python script for data preprocessing.


