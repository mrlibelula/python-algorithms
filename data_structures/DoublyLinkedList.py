class Node:
    def __init__(self, data = None, next = None, prev = None) -> None:
        self.data = data
        self.next = next
        self.prev = prev
        
class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        
    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next
            
        return itr
    
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
            
        return count
        
    def print_forward(self):
        if self.head is None:
            print('Doubly linked list is empty')
            return
        
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + (' -> ' if itr.next else '')
            itr = itr.next
        print('Forward list : ', llstr)
        
    def print_backward(self):
        if self.head is None:
            print('Doubly linked list is empty')
            return
        
        last_node = self.get_last_node()
        itr = last_node
        llstr = ''
        
        while itr:
            llstr += str(itr.data) + (' -> ' if itr.prev else '')
            itr = itr.prev
            
        print('Reversed list: ', llstr)
        
    def insert_at_begining(self, data):
        node = Node(data, self.head, None)
        if self.head == None:
            self.head = node
        else:
            self.head.prev = node
            self.head = node
            
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
            
        itr.next = Node(data, None, itr)
        
    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception('Invalid index')
        
        if index == 0:
            self.insert_at_begining(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next, itr)
                if node.next:
                    node.next.prev = node
                itr.next = node
                break
            
            itr = itr.next
            count += 1

if __name__ == '__main__':
    dl = DoublyLinkedList()
    dl.insert_at_begining(20)
    dl.insert_at_begining(10)
    dl.insert_at_begining(5)
    dl.insert_at_end(99)
    dl.insert_at(2, 678)
    dl.print_forward()
    dl.print_backward()