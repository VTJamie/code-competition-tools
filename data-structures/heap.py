import heapq
import json

class Heap:
    def __init__(self, basevalues = [], multiplier = 1):
        self.heap = list(map(lambda x: x*multiplier, basevalues))
        self.multiplier = multiplier
        heapq.heapify(self.heap)
    def peek(self):
        if len(self.heap) > 0:
            return self.heap[0]*self.multiplier
        return None

    def length(self):
        return len(self.heap)

    def add(self, value):
        heapq.heappush(self.heap, value*self.multiplier)

    def pop(self):
        return heapq.heappop(self.heap)*self.multiplier

    def debug(self):
        mult = self.multiplier
        print(json.dumps(list(map(lambda x: x*mult, self.heap)), indent=2))

class MaxHeap(Heap):
    def __init__(self, basevalues = []):        
        Heap.__init__(self, basevalues, -1)       
        

class MinHeap(Heap):
    def __init__(self, basevalues = []): 
        Heap.__init__(self, basevalues, 1)       
        

if __name__ == '__main__':
    minheap = MinHeap([4, 2, 1])
    maxheap = MaxHeap([1, 2, 3])

    
    
    print(minheap.peek())
    print(minheap.pop())
    print(minheap.peek())
    print(minheap.debug())
    #print(maxheap.peek())