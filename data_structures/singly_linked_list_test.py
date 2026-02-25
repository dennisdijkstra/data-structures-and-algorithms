from data_structures.singly_linked_list import SinglyLinkedList


def test_singly_linked_list_init():
    linked_list = SinglyLinkedList()

    assert linked_list.size == 0
    assert linked_list.head == None


def test_singly_linked_list_insert_head():
    linked_list = SinglyLinkedList()
    value = "head"
    linked_list.insert_head(value)

    assert linked_list.size == 1
    assert linked_list.head.value == value


def test_singly_linked_list_insert_tail():
    linked_list = SinglyLinkedList()
    value_one = "head"
    value_two = "tail"
    linked_list.insert_head(value_one)
    linked_list.insert_tail(value_two)

    assert linked_list.size == 2


def test_singly_linked_list_insert():
    linked_list = SinglyLinkedList()
    value_one = "head"
    value_two = "any"
    linked_list.insert_head(value_one)
    linked_list.insert(value_two, 1)

    assert linked_list.size == 2
    assert linked_list.get(1).value == value_two


def test_singly_linked_list_remove_head():
    linked_list = SinglyLinkedList()
    value_one = "a"
    value_two = "b"
    value_three = "c"

    linked_list.insert(value_one, 0)
    linked_list.insert(value_two, 1)
    linked_list.insert(value_three, 2)
    linked_list.remove_head()

    assert linked_list.size == 2
    assert linked_list.head.value == value_two


def test_singly_linked_list_remove_tail():
    linked_list = SinglyLinkedList()
    value_one = "a"
    value_two = "b"
    value_three = "c"

    linked_list.insert(value_one, 0)
    linked_list.insert(value_two, 1)
    linked_list.insert(value_three, 2)
    linked_list.remove_tail()

    assert linked_list.size == 2
    assert linked_list.get(1).value == value_two


def test_singly_linked_list_remove():
    linked_list = SinglyLinkedList()
    value_one = "a"
    value_two = "b"
    value_three = "c"

    linked_list.insert(value_one, 0)
    linked_list.insert(value_two, 1)
    linked_list.insert(value_three, 2)
    linked_list.remove(1)

    assert linked_list.size == 2
    assert linked_list.get(1).value == value_three


def test_singly_linked_list_update():
    linked_list = SinglyLinkedList()
    value_one = "a"
    value_two = "b"
    value_three = "c"

    linked_list.insert(value_one, 0)
    linked_list.insert(value_two, 1)
    linked_list.update(value_three, 1)

    assert linked_list.size == 2
    assert linked_list.get(1).value == value_three


def test_singly_linked_list_get():
    linked_list = SinglyLinkedList()
    value_one = "a"
    value_two = "b"

    linked_list.insert_head(value_one)
    linked_list.insert(value_two, 1)
    head = linked_list.get(0)

    assert head.value == value_one


def test_singly_linked_list_get_out_of_range():
    linked_list = SinglyLinkedList()
    value_one = "a"
    value_two = "b"

    linked_list.insert_head(value_one)
    linked_list.insert(value_two, 1)
    some_node = linked_list.get(5)

    assert some_node == None
