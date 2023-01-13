from Queue import *
        
q1 = Queue()

q1.new(4)
q1.enqueue('J')
q1.enqueue('K')
q1.enqueue('L')
#q1.show()

print(q1.dequeue())
#q1.show()
q1.enqueue('M')
#q1.show()

print(q1.dequeue())
#q1.show()
q1.enqueue('N')
q1.enqueue('P')
#q1.show()

print(q1.dequeue())
print(q1.dequeue())
#q1.show()

q1.enqueue('Q')
#q1.show()
print(q1.dequeue())
#q1.show()
q1.enqueue('R')
#q1.show()
print(q1.dequeue())
print(q1.dequeue())


