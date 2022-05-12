class haralickResult:
    
    def __init__(self, gcm, ener, entr, homog):
        self.matriz_cooc = gcm
        self.energy = ener
        self.entropy = entr
        self.homogeneity = homog
        