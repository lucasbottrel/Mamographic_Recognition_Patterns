from skimage import data
from skimage.feature import graycomatrix, graycoprops
from skimage.measure import shannon_entropy
from skimage.morphology import disk, ball
from skimage import *
import numpy as np

def haralick_calcs(img_calc):
    
    gcm_1 = graycomatrix(img_calc, [1], [0, np.pi/4, np.pi/2, 3*np.pi/4])
    gcm_2 = graycomatrix(img_calc, [1, 2], [0, np.pi/4, np.pi/2, 3*np.pi/4])
    gcm_4 = graycomatrix(img_calc, [1, 4], [0, np.pi/4, np.pi/2, 3*np.pi/4])
    gcm_8 = graycomatrix(img_calc, [1, 8], [0, np.pi/4, np.pi/2, 3*np.pi/4])
    gcm_16 = graycomatrix(img_calc, [1, 16], [0, np.pi/4, np.pi/2, 3*np.pi/4])
    
    haralick_1 = {
        'matriz_cooc': gcm_1,
        'entropia': shannon_entropy(gcm_1, base=2),
        'energy': graycoprops(gcm_1, 'energy')[0,0],
        'homogeneity': graycoprops(gcm_1, 'homogeneity')[0,0]
    }
    
    haralick_2 = {
        'matriz_cooc': gcm_2,
        'entropia': shannon_entropy(gcm_2, base=2),
        'energy': graycoprops(gcm_2, 'energy')[0,0],
        'homogeneity': graycoprops(gcm_2, 'homogeneity')[0,0]
    }
    
    haralick_4 = {
        'matriz_cooc': gcm_4,
        'entropia': shannon_entropy(gcm_4, base=2),
        'energy': graycoprops(gcm_4, 'energy')[0,0],
        'homogeneity': graycoprops(gcm_1, 'homogeneity')[0,0]
    }
    
    haralick_8 = {
        'matriz_cooc': gcm_8,
        'entropia': shannon_entropy(gcm_8, base=2),
        'energy': graycoprops(gcm_8, 'energy')[0,0],
        'homogeneity': graycoprops(gcm_8, 'homogeneity')[0,0]
    }
    
    haralick_16 = {
        'matriz_cooc': gcm_16,
        'entropia': shannon_entropy(gcm_16, base=2),
        'energy': graycoprops(gcm_16, 'energy')[0,0],
        'homogeneity': graycoprops(gcm_16, 'homogeneity')[0,0]
    }
    
    return [haralick_1, haralick_2, haralick_4, haralick_8, haralick_16]