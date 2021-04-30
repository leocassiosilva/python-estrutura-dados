from collections import defaultdict
import heapq
#min heap 
class MinHeap:
    
    def __init__(self):
        self._queue = []
        self._index = 0
    
    def insert(self, item, prioridade):
        heapq.heqppush(self._queue, (-prioridade, self._index, item))
        self._index += 1
    
    def remove(self):
        return heapq.heappop(self._queue)[-1]
    
    def get_length(self):
        return len(self._queue)