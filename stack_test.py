from stack import Stack

def test_stack_init():
  stack = Stack()

  assert stack.size == 0
  assert stack.is_empty() == True

def test_stack_push():
  stack = Stack()

  stack.push(1)
  stack.push(2)

  assert stack.size == 2
  assert stack.peek() == 2
  assert stack.is_empty() == False

def test_stack_pop():
  stack = Stack()

  stack.push(1)
  stack.push(2)
  stack.push(3)
  stack.pop()

  assert stack.size == 2
  assert stack.peek() == 2
  assert stack.is_empty() == False