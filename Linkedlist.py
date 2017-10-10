class Node:
    def __init__(self, data = None, nextNode = None):
        self.data = data
        self.next = nextNode

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self,newNode):
        self.next = newNode

    def set_data(self,data):
        self.data = data


class LinkedList(object):
    def __init__(self, head = None,last = None):
        self.head = head
        self.last = last

    def insert(self,data):
        node = Node(data)
        node.set_next(self.head)
        if(self.head == None):
            self.head = node
            self.last = node
        else:
            self.head = node

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()

        return count

    def search(self, data):
        current = self.head
        found = -1
        position = 0
        while current and found == -1 :
            position += 1
            if(current.get_data() == data):
                found = 1
            else:
                current = current.get_next()

        if current is None:
            return ("No element")

        return "The position of the element is at",position

    def delete(self,data):
        current = self.head
        previous = None
        found = -1
        while current and found == -1:
            if(current.get_data() == data):
                found = 1
            else:
                previous = current
                current = current.get_next()

        if current is None:
            raise ValueError("No data")

        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def print(self):
        current = self.head
        while current:
            print(current.get_data())
            current = current.get_next()



    def get_middleelement(self, size):
        current = self.head
        counter = 1
        while (counter <= size):
            if(counter%2 == 0):
                current = current.get_next()
            else:
                previous = current.get_next()
            counter += 1

        return("The middle most element is", current.get_data())

    def Bubblesort(self):
        prev = self.head
        current = self.head.get_next()

        while current:
            if prev == None:
                return ("No obejcts in the list")
            elif (prev.get_data() > current.get_data()):
                temp = prev.get_data()
                prev.set_data(current.get_data())
                current.set_data(temp)
            prev = current
            current = current.get_next()

    def divideLists(self):
        slow = self.head
        fast = self.head.get_next()
        while fast:
            fast = fast.get_next()
            if fast:
                fast = fast.get_next()
                slow = slow.get_next()
        mid = slow.get_next()
        slow.set_next(None)
        return self.head,mid

    def mergeLists(self,l1,l2):
        temp = None
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.get_data() <= l2.get_data():
            temp = l1
            temp.next = self.mergeLists(l1.get_next(), l2)
        else:
            temp = l2
            temp.next = self.mergeLists(l1, l2.get_next())
        return temp

    def mergeSort(self):
        if self.head is None or self.head.get_next() is None:
            return self.head
        else:
            list1,list2 = self.divideLists()
            list1 = self.mergeSort()
            list2 = self.mergeSort()
            head = self.mergeLists(list1,list2)

        return head



linked = LinkedList()
linked.insert(9)
linked.insert(10)
linked.insert(8)
linked.insert(7)
linked.insert(6)
#linked.print()
linked.mergeSort()
#linked.print()


