from Queue import *
        
q2 = Queue()
q2.new(4)
q2.enqueue(15)
q2.enqueue(28)
print(q2.dequeue())
q2.enqueue(31)
print(q2.peek())
print(q2.dequeue())
print(q2.dequeue())
q2.enqueue(47)
print(q2.peek())
q2.enqueue(54)
print(q2.dequeue())
q2.enqueue(66)
q2.clear()
q2.enqueue(79)
print(q2.dequeue())


