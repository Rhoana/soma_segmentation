import h5py

import numpy as np

"/Users/tim/Documents/TMI_Revision/SomaeDetection/Mouse/gt_data/seg_Mouse_762x832x832.h5"

def ReadH5File(filename,box):
    # return the first h5 dataset from this file
    with h5py.File(filename, 'r') as hf:
        keys = [key for key in hf.keys()]
        d = hf[keys[0]]
        data=np.array(d)

    return data

def WriteH5File(data, filename, dataset):
    with h5py.File(filename, 'w') as hf:
        hf.create_dataset(dataset, data=data, compression='gzip')