from collections import defaultdict
import heapq
#min heap 
class MinHeap:
    
    def __init__(self):
        self._queue = []
        self._index = 0
    
    def insert(self, item, prioridade):
        heapq.heappush(self._queue, (-prioridade, self._index, item))
        self._index += 1
    
    def remove(self):
        return heapq.heappop(self._queue)[-1]
    
    def get_length(self):
        return len(self._queue)



#criando um grafo
class Grafo:

    def __init__(self):
        self.grafo = defaultdict(list)
        self.vertexes = {}

    def addEdge(self, src, dest, cost):
        self.grafo[src].append((dest, cost))
        self.vertexes[src] = src
        self.vertexes[dest] = dest

    def dijkstra(self, src, dest):
        
        #obtem o número de vértices
        numero_vertices = len(self.vertexes)

        #estimativas de menor custo
        p = [None for i in range(numero_vertices)]

        #estima para origem é 0
        p[src] = 0

        #controi a min
        min_heap = MinHeap()

        #insere a origem na min heap 
        min_heap.insert(src, 0)

        #enquanto o tamanho da fila for maior que 0
        while min_heap.get_length() > 0:

            #remove da fila de prioridades
            u = min_heap.remove()

            #percorre os adjacentes de "u"
            for edge in self.grafo[u]:

                #obtém o vertice adjacente e o custo
                v, cost = edge

                #relaxamento
                if p[v] is None or p[v] > p[u] + cost:

                    #atualiza a estimativa de custo
                    p[v] = p[u] + cost

                    #insere na fila de prioridades
                    min_heap.insert(v, p[v])
        
        #retorna o custo do menor caminho
        return p[dest]
                    

g = Grafo()
g.addEdge(0, 1, 1)
g.addEdge(0, 3, 3)
g.addEdge(0, 4, 10)
g.addEdge(1, 2, 5)
g.addEdge(2, 4, 1)
g.addEdge(3, 2, 2)
g.addEdge(3, 4, 6)

print(g.dijkstra(0, 4))