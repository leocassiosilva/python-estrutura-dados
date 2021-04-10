#implementação da rede neural perceptron

'''
w =w N *(d(k) - y) * x(k)
'''
class Perceptron:
    
    def __init__(self, amostras, saidas, taxa_aprendizado=0.1, epocas=1000, limiar=-1):

        self.amostras = amostras #todas as amostras
        self.saidas = saidas #saidas respectivas de cada amostra
        self.taxa_aprendizado =taxa_aprendizado #taxa de aprendizagem (entre 0 e 1)
        self.epocas = epocas #numero de epocas
        self.limiar = limiar
        self.num_amostras = len(amostras) #quantidade de amostras
        self.num_amostra = len(amostras[0]) #quantidade de elementos por amostra
        self.pesos = [] #vetor de pesos


    #vetor de pesos
    def treinar(self):
        pass
        