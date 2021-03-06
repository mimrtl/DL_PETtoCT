'''
Helena Van Hemmen, May 2020
for PDFF and R2 quantification project
'''
import os
import glob
import numpy as np
import scipy.io as spio
import pandas as pd

in_ch = 2
out_ch = 3

data_folder = '/Users/helenavanhemmen/Desktop/Folder/MIMRTL/DLforPDFFandR2_Data/Ideal_data1p5'

def prepare():
    
    np.random.seed(813)

    print('Loading images from' + data_folder + '...')

    input_count = 0
    for filename in os.listdir(data_folder):
        if (not filename.startswith('00')) and filename.endswith('.mat'):
        
            input_count += 1

            curr_input = spio.loadmat(data_folder + '/' + filename, struct_as_record = True)

            img_idata = curr_input['img_idata']
            img_ref = curr_input['img_ref']

            inputs = {}
            for x in range(12):
                inputs['in_ch_' + str(x)] = img_idata[:,:,:,x]

            in_df = pd.DataFrame(inputs)

            outputs = {}
            outputs['water'] = img_ref[:,:,:,0]
            outputs['fat'] = img_ref[:,:,:,1]
            outputs['r2'] = img_ref[:,:,:,2]

            out_df = pd.Dataframe(outputs)

        else:
            continue

prepare()






        