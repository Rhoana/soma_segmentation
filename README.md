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
We provide examples for both training and prediction. The training data is taken from the JWR dataset [1]. The segmentation as well as the soma mask can be found in the folder *Training_Data*. The soma mask is a binary tensor that was manually created by us. The segmentation for which somata are is taken from the Zebrafinch dataset [2] and can be found in the folder *Prediction_Data*. We further provide the trained network in *Trained_Network*, which was achieved by training on the JWR data. This network has been used for the somata predictions on the Zebrafinch data that is presented in our paper. 

## Running Training and Prediction
To train a new network, run ```python run_training.py```.
To predict the somata of an input segmentation with a pretrained network, run ```python run_prediction.py```.

[1] Lin, Zudi, et al. "Two Stream Active Query Suggestion for Active Learning in Connectomics." Computer Vision–ECCV 2020: 16th European Conference, Glasgow, UK, August 23–28, 2020, Proceedings, Part XVIII 16. Springer International Publishing, 2020.  
[2] Kornfeld, Jörgen, et al. "EM connectomics reveals axonal target variation in a sequence-generating network." Elife 6 (2017): e24364.  
