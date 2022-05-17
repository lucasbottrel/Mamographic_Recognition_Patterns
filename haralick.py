from haralickResult import haralickResult
from skimage.feature import graycomatrix, graycoprops
from skimage.measure import shannon_entropy
from skimage import *
import numpy as np

#def matrixSum(gcm_1, gcm_2, gcm_4, gcm_8, gcm_16):
#   for i in range(96):
    # for j in range(len(resampled_img)):
    #   for j in range(len(resampled_img)):
     #     resampled_img[i][j] = resampled_img[i][j] / maxValue * shades

# calculate haralick parameters
def haralick_calcs(img_calc):
    
    # comatrix for each distance
    gcm_1 = graycomatrix(img_calc, [1], [0, np.pi/4, np.pi/2, 3*np.pi/4])
    gcm_2 = graycomatrix(img_calc, [2], [0, np.pi/4, np.pi/2, 3*np.pi/4])
    gcm_4 = graycomatrix(img_calc, [4], [0, np.pi/4, np.pi/2, 3*np.pi/4])
    gcm_8 = graycomatrix(img_calc, [8], [0, np.pi/4, np.pi/2, 3*np.pi/4])
    gcm_16 = graycomatrix(img_calc, [16], [0, np.pi/4, np.pi/2, 3*np.pi/4])
    
    # create object per matrix generated
    haralick_1 = haralickResult(
        gcm_1,
        graycoprops(gcm_1, 'energy')[0,0],
        shannon_entropy(gcm_1),
        graycoprops(gcm_1, 'homogeneity')[0,0],
        graycoprops(gcm_1, 'contrast')[0,0],
        graycoprops(gcm_1, 'dissimilarity')[0,0],
        graycoprops(gcm_1, 'ASM')[0,0],
        graycoprops(gcm_1, 'correlation')[0,0]
    )
    
    haralick_2 = haralickResult(
        gcm_2,
        graycoprops(gcm_2, 'energy')[0,0],
        shannon_entropy(gcm_2),
        graycoprops(gcm_2, 'homogeneity')[0,0],
        graycoprops(gcm_2, 'contrast')[0,0],
        graycoprops(gcm_2, 'dissimilarity')[0,0],
        graycoprops(gcm_2, 'ASM')[0,0],
        graycoprops(gcm_2, 'correlation')[0,0]
    )
    
    haralick_4 = haralickResult(
        gcm_4,
        graycoprops(gcm_4, 'energy')[0,0],
        shannon_entropy(gcm_4),
        graycoprops(gcm_4, 'homogeneity')[0,0],
        graycoprops(gcm_4, 'contrast')[0,0],
        graycoprops(gcm_4, 'dissimilarity')[0,0],
        graycoprops(gcm_4, 'ASM')[0,0],
        graycoprops(gcm_4, 'correlation')[0,0]
    )
    
    haralick_8 = haralickResult(
        gcm_8,
        graycoprops(gcm_8, 'energy')[0,0],
        shannon_entropy(gcm_8),
        graycoprops(gcm_8, 'homogeneity')[0,0],
        graycoprops(gcm_8, 'contrast')[0,0],
        graycoprops(gcm_8, 'dissimilarity')[0,0],
        graycoprops(gcm_8, 'ASM')[0,0],
        graycoprops(gcm_8, 'correlation')[0,0]
    )
    
    haralick_16 = haralickResult(
        gcm_16,
        graycoprops(gcm_16, 'energy')[0,0],
        shannon_entropy(gcm_16),
        graycoprops(gcm_16, 'homogeneity')[0,0],
        graycoprops(gcm_16, 'contrast')[0,0],
        graycoprops(gcm_16, 'dissimilarity')[0,0],
        graycoprops(gcm_16, 'ASM')[0,0],
        graycoprops(gcm_16, 'correlation')[0,0]
    )
    
    return [haralick_1, haralick_2, haralick_4, haralick_8, haralick_16]