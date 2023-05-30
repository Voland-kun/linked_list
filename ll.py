class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self, node: Node):
        self.head = node

    def reverse_list(self):
        val = self.head
        tail = None
        while val:
            val.next, tail, val = tail, val, val.next
        return tail
    
    def print_list(self):
        node = self.head
        while node:
            print(node.val)
            node = node.next
        print()

    def find_elem_from_end(self, target):
        if self.head == None:
            return False
        val = self.head
        count = 1 # 0 если отсчёт числа с конца от нуля
        while val:
            if count == target:
                val2 = self.head                
            elif count > target:
                val2 = val2.next
            count += 1
            val = val.next
        return val2.val

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
ll = LinkedList(node1)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
print('Заданный список')
ll.print_list()
print(f'Элемент с конца {ll.find_elem_from_end(3)} \n')
ll.head = ll.reverse_list()
print('Перевернутый список')
ll.print_list()
