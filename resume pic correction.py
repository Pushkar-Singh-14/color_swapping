import cv2
import numpy as np
import os

path="/Users/pushkarsingh/Downloads/resume icons/cvr"
blue=230
green=160
red=0

path_save=os.path.join(path,f'{blue}-{red}-{green}-Data-pic')
        
color=[230,0,160]

if not os.path.exists(path_save):
    os.makedirs(path_save)

for files in os.listdir(path):
##    print(files)
    file_ext=os.path.splitext(files)[1]
    if file_ext==".png":
        file= os.path.join(path,files)
        file_name=os.path.splitext(files)[0]

        src = cv2.imread(file,cv2.IMREAD_UNCHANGED)
        
        bgr = src[:,:,:3] # Channels 0..2
        '''
        gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
        Gauss_threshold =cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,101,10)

        ### Some sort of processing...
        ##gray[np.where(gray == [0])] = [123]

        bgr = cv2.cvtColor(Gauss_threshold, cv2.COLOR_GRAY2BGR)
        '''
        bgr[np.where((bgr == [0,0,0]).all(axis = 2))] = color1
        
        alpha = src[:,:,3] # Channel 3
        result = np.dstack([bgr, alpha]) # Add the alpha channel
        
        file_name=os.path.splitext(files)[0]
        save_file=os.path.join(path_save,files)

        cv2.imwrite(save_file, result)
        
