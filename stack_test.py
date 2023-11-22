from stack import Stack

def test_stack_init():
  stack = Stack()

  assert stack.size == 0
  assert bool(stack) == True