class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

class LinkedList :
    def __init__(self, data) :
        self.head = Node(data)
    
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
        while test_subject != None :
            print(test_subject)
            test_subject = test_subject.next
        test_subject = Node(next_data)
        self.head.next = Node(next_data)