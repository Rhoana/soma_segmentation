## Setup
```
git clone https://github.com/fratim/detectSomata  

cd detectSomata  

conda create -n SomataDetection --file requirements.txt  

conda activate SomataDetection  
```

## Parameter Specification
All parameter must be specified in ```parameters.py```. Most importantly, the correct filepaths for the training segmentation, the corresponding soma mask and the segmentation for which the somata shall be predicted.

## Example Data and trained Model
We provide examples for both training and prediction. The training data is taken from the JWR dataset [TODO add reference]. The segmentation as well as the soma mask can be found in the folder *Training_Data*. The soma mask is a binary tensor that was manually created by us. The segmentation for which somata are is taken from the Zebrafinch dataset [TODO add reference] and can be found in the folder *Prediction_Data*. We further provide the trained network in *Trained_Network*, which was achieved by training on the JWR data. This network has been used for the somata predictions on the Zebrafinch data that is presented in our paper. 

## Running Training and Prediction
To train a new network, run ```python run_training.py```.
To predict the somata of an input segmentation with a pretrained network, run ```python run_prediction.py```.
