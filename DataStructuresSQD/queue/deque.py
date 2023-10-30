class DeQueue:
    def __init__(self):
        self.items = []

    def add_front(self, item):
        """
            This method adds items to the front of a list 
            this happens in constant time 0(1)
        """
        self.items.insert(0, item)

    def add_rear(self, item):
        """
            This method appends element to the end of the list 
            This happens in constant time
        """
        self.items.append(item)

    def remove_rear(self):
        """
            This method removes element from the end of the list 
            This happens in constant time
        """
        if self.items:
            return self.items.pop()
        return None

    def remove_front(self):
        """
            This method removes element from the start (front) of the list 
            This happens in constant time
        """
        if self.items:
            return self.items.pop(0)
        return None

    def peek_front(self):
        """
            This method returns the element infront (start) of the list 
            This happens in constant time
        """
        if self.items:
            return self.items[0]
        return None

    def peek_rear(self):
        """
            This method returns the next element at the end of the list 
            This happens in constant time
        """
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        """
            This method returns the size of the list (the lenght of the list)
            This happens in constant time
        """
        return len(self.items)

    def is_empty(self):
        """
            This method returns true or false depending on the contents
            of the list, either empty or not empty
            This happens in constant time
        """
        return self.items == []


def main():
    my_dq = DeQueue()
    my_dq.add_rear("banana")
    my_dq.add_rear("apple")
    my_dq.add_rear("mango")
    my_dq.add_front("Oranges")
    print(my_dq.items)
    print(my_dq.remove_rear())
    print(my_dq.remove_front())
    print(my_dq.items)


if __name__ == "__main__":
    main()
