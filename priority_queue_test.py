from priority_queue import PriorityQueue

def test_priority_queue_init():
  queue = PriorityQueue()
  
  assert queue.size == 0
  assert bool(queue) == True
  
def test_priority_queue_enqueue():
  queue = PriorityQueue()
  
  queue.enqueue({ 'value': 'A', 'priority': 2 })
  queue.enqueue({ 'value': 'B', 'priority': 10 })
  queue.enqueue({ 'value': 'C', 'priority': 6 })
  
  assert queue.size == 3
  assert queue.peek()['value'] == 'B' 
  
def test_priority_queue_dequeue():
  queue = PriorityQueue()
  
  queue.enqueue({ 'value': 'A', 'priority': 12 })
  queue.enqueue({ 'value': 'B', 'priority': 5 })
  queue.enqueue({ 'value': 'C', 'priority': 1 })
  queue.enqueue({ 'value': 'D', 'priority': 4 })
  queue.dequeue()
  queue.dequeue()
  
  assert queue.size == 2
  assert queue.peek()['value'] == 'D' 

def test_priority_queue_peek():
  queue = PriorityQueue()
  
  assert queue.peek() == None

  queue.enqueue({ 'value': 'A', 'priority': 0 })
  queue.enqueue({ 'value': 'B', 'priority': 1 })
  assert queue.peek()['value'] == 'B' 
