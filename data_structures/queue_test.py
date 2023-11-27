from queue_ import Queue

def test_queue_init():
  queue = Queue()

  assert queue.size == 0
  assert bool(queue) == True

def test_queue_enqueue():
  queue = Queue()

  queue.enqueue(1)
  queue.enqueue(2)

  assert queue.size == 2
  assert queue.peek() == 1

def test_queue_dequeue():
  queue = Queue()

  queue.enqueue(1)
  queue.enqueue(2)
  queue.enqueue(3)
  queue.dequeue()

  assert queue.size == 2
  assert queue.peek() == 2
