class ArrayQueue:
    """FIFO queue implementation using a python list as underlying storage"""
    DEFAULT_CAPACITY = 10   
    
    def __init__(self) -> None:
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def first(self):
        if self.is_empty(): raise Exception("Queue is empty")
        return self._data[self._front]
    
    def dequeue(self):
        """fill space with None
         Adjust size, front
         return answer
        O(1)
        """
        if self.is_empty(): 
            raise Exception("Queue is empty")
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if 0 < self._size < len(self._data) //4:
            self._resize(len(self._data) // 2)

        return answer
    
    def enqueue(self, e):
        """Add element to the back of the queue"""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        
        available =  (self._front + self._size) % len(self._data)
        self._data[available] = e
        self._size += 1
    
    def _resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)

        self._front = 0
    
    
    
    def __str__(self) -> str:

        print(self._data)
     


if __name__ == '__main__':
    Q = ArrayQueue()
    Q.enqueue(5)
    Q.enqueue(3)
    Q.__str__()
    print("Length of queue is {}".format(len(Q)))
    for i in range(0, 11):
        Q.enqueue(i)
    Q.__str__()

    
    
