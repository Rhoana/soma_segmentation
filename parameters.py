## model parameters ##
# input size (x==y)
network_size = 832
# depth of input tensor
depth = 4
# learning rate used
learning_rate = 0.001
# training epochs
epochs = 500
# batch size used (depending on computing ressources)
batch_size = 4

## other parameters ##
# number of given slices to use for validation
val_data_size = 384

## parameters for prediction ##
ckpt_restore = '../SomaeDetection/ckpt/-40'

# filepaths
train_seg_in_filepath = "Mouse/seg_Mouse_762x832x832.h5"
train_somae_in_filepath = "Mouse/somae_Mouse_762x832x832.h5"
predict_seg_in_filepath = "Zebrafinch/Zebrafinch-seg_filled-dsp8.h5"
somae_prediction_out_filepath = "Zebrafinch/Zebrafinch-somae_filled_new-dsp_8_2021.h5"
