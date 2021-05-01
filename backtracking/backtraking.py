#Gerando todos os subconjuntos com backtracking
def gerar_sub_cnjuntos(S, vet, K, N):
    if K == N:
        for i in range(N):
            if vet[i] == True:
                print('%d' % S[i], end=' ')
        print('')
    else:
        vet[K]= True
        gerar_sub_cnjuntos(S, vet, K + 1, N)
        vet[K]= False
        gerar_sub_cnjuntos(S, vet, K + 1, N)


S = [1, 2]
vet = [False for i in range(len(S))]

gerar_sub_cnjuntos(S, vet, 0, len(S))
