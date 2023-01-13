from Queue import *

q3 = Queue()
q3.new(4)
print(q3.is_empty())
q3.enqueue("pawikan")
q3.enqueue("tarsier")
print(q3.peek())
print(q3.dequeue())
print(q3.is_empty())
print(q3.dequeue())
print(q3.dequeue())
q3.enqueue("tuko")
q3.enqueue("tamaraw")
q3.enqueue("dugong")
print(q3.dequeue())
q3.enqueue("haribon")
q3.enqueue("butanding")
q3.enqueue("bayawak")



