from skimage.filters import gaussian
from skimage.filters import threshold_otsu
from skimage.restoration import denoise_bilateral
from skimage.morphology import skeletonize
import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
import os





def trial_no_02(refimage, testimg):
    img = testimg-refimage
    img_gray=rgb2gray(img)
    #out2=img_gray>ref_thr
    #plt.imshow(out2,cmap='gray')
    image,(ax1,ax2,ax3) = plt.subplots(nrows=3,ncols=1)
    plt.axis('off')
    ax1.imshow(refimage)
    ax1.set_title('reference image')
    ax2.imshow(testimg)
    ax2.set_title('actual  image')
    ax3.imshow(img_gray, cmap='gray')
    ax3.set_title('output image')
    ax1.axis('off')
    ax2.axis('off')
    ax3.axis('off')

    plt.show()




if __name__ == '__main__':
    path = 'C:/Users/mohri/Documents/python files/pcb project/'
    refpath = os.path.join(path, 'pcb3.jpg')
    testpath = os.path.join(path, 'pcb3_defective.jpg')
    refimg = plt.imread(refpath)
    testimg = plt.imread(testpath)
    trial_no_02(refimg, testimg)
