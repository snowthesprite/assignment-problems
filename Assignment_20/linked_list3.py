class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None
        self.index = None

class LinkedList :
    def __init__(self, data) :
        self.head = Node(data)
        self.head.index = 0

    def set_index(self) :
        index = 0
        node = self.head
        while node != None :
            node.index = index
            index += 1
            node = node.next
    
    def print_data(self) :
        test_subject = self.head
        while test_subject != None :
            print(test_subject.data)
            test_subject = test_subject.next

    def length(self) :
        count = 0
        test_subject = self.head
        while test_subject != None :
            count += 1
            test_subject = test_subject.next
        return count

    def append(self, next_data) :
        test_subject = self.head
        while test_subject.next != None :
            test_subject = test_subject.next
        test_subject.next = Node(next_data)
        self.set_index()

    def push(self, new_data) :
        data = Node(new_data)
        old_head = self.head
        data.next = old_head
        self.head = data
        self.set_index()

    def get_node(self, index) :
        node = self.head
        while node != None :
            if node.index == index :
                return node
            node = node.next
    
    def delete(self,index) :
        node = self.head
        while node.next.index != index :
            node = node.next
        return node.next
