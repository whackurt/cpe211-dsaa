class Queue:
    maxQsize = 0
    front = -1
    rear = -1
    que = []
    
    def __init__(self):
        pass
    
    def new(self, max_size):
        self.maxQsize = max_size
        return self.que

    def clear(self):
        if self.is_empty():
            print("Warning: Queue is empty.")
        else:
            self.que.clear()
            self.front = -1
            self.rear = -1
            
        
    def is_empty(self):
        # return self.front == -1
        return len(self.que) == 0
    
    def is_full(self):
        return self.rear == self.maxQsize-1
    
    def enqueue(self, itemToEnqueue):
        if self.is_full():
            print("Error: Queue is full")
        else:
            self.que.append(itemToEnqueue)
            self.front = 0
            self.rear += 1
            
    def dequeue(self):
        if self.is_empty():
            print("Error: Queue is empty.")
        else:
            toDequeue = self.que[self.front]
            
            if self.front == self.rear:
                self.clear()
            else:
                self.que.remove(toDequeue)
                self.rear -= 1
                
            return toDequeue
            
    def peek(self):
        return self.que[self.rear]
    
    def size(self):
        length = 0
        for item in self.que:
            length += 1
        return length
    
    def show(self):
        print(self.que)   