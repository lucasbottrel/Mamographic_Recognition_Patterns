import numpy as np

#function to calculate the entropy of the image
def entropy(im):
    # Compute normalized histogram 
    p = np.array([(im==v).sum() for v in range(256)])
    p = p/p.sum()
    # Compute e = -sum(p(g)*log2(p(g)))
    e = -(p[p>0]*np.log2(p[p>0])).sum()
    
    return e

