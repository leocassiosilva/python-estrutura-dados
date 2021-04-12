#implementação da rede neural perceptron

'''
w =w N *(d(k) - y) * x(k)
'''
import random, copy
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


    #essa função serve para treinar a rede
    def treinar(self):

        #adicionar -1 para cada uma das amostras
        for amostra in self.amostras:
            amostra.insert(0, -1)

        #inicia o vetor de pesos com valores aleatórios
        for i in range(self.num_amostra):
            self.pesos.append(random.random())
        
        #insere o limiar ao vetor de pesos
        self.pesos.insert(0, self.limiar)

        #inicia o contador de epocas
        num_epocas = 0

        while True:

            erro = False #erro inicialmente inexiste

            #para todas as amostrars de treinamento
            for i in range(self.num_amostras):
                u = 0
                

                '''
                realiza o somatório, o limite (se.amostra + 1)
                é porque foi inserido o -1 para cada amostra
                '''
                for j in range(self.num_amostra +1):
                    u += self.pesos[j] * self.amostras[i][j]

                
                y = self.sinal(u)

                if y != self.saidas[i]: 
                    
                    #calcula o erro: subtração entre saida desejada e a saida da rede
                    erro_aux = self.saidas[i] - y

                    #faz o ajuste dos pesos para cada elemento da amostra
                    for j in range(self.num_amostra + 1):
                        self.pesos[j] = self.pesos[j] + self.taxa_aprendizado * erro_aux * self.amostras[i][j]

                    erro = True # ainda existe erro

                #incrementa o numero de epocas
                num_epocas +=1

                #critero de parada é pelo número de épocas ou se não existir erro
                if num_epocas > self.epocas or not erro:
                    break

    #função utilizada para testar a rede
    #receve uma amostra a ser classificada e os nomes das classes
    #utiiza a funçao sinal, se é 1 então é classe1, se não é classe2
    def testar(self, amostra, classe1, classe2):

        #insere 0 -1 
        amostra.insert(0, -1)

        #utiliza o vetor de pesos que foi ajustado na fase de treinamento
        u = 0
        for i in range(self.num_amostra + 1):
            u += self.pesos[i] * amostra[i]

        #calculando a saída da rede 
        y = self.sinal(u)

        #verifica a qual classe pertence
        if y == -1:
            print('A amostra pertence a classe %s ' % classe1)
        else:
            print('A amostra pertence a classe %s ' % classe2)

    #função de ativação: degrau bipolar (sinal)
    def sinal(self, u): 
        return 1 if u >= 0 else 1

print('\n A ou B?\n')

#amostras: um total de 4 amostras
amostras = [[0.1, 0.4, 0.7], [0.3, 0.7, 0.2], [0.6, 0.9, 0.8], [0.5, 0.7, 0.1]]

#saida desejada de cada amostra
saidas = [1, -1, -1, 1]

#conjunto de amostras de testes 
testes = copy.deepcopy(amostras)

rede = Perceptron(amostras=amostras, saidas=saidas, taxa_aprendizado=0.1, epocas=1000)


# treina a rede
rede.treinar()

# testando a rede
for teste in testes:
	rede.testar(teste, 'A', 'B')