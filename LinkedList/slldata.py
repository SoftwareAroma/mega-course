class SLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"SLLNode object: data = {self.data}"

    def get_data(self):
        """
            This method returns the data 
        """
        return self.data

    def set_data(self, new_data):
        """
            replace the existing data with a new
            data
        """
        self.data = new_data

    def get_next(self):
        """
            returns the next item in the linked
            list
        """
        return self.next

    def set_next(self, new_next):
        """
            Replace the next value with a new
            value
        """
        self.next = new_next


class SLL:
    def __init__(self):
        self.head = None

    def __repr__(self):
        return f"SLL object: head = {self.head}"

    def is_empty(self):
        """
            This return tru or false based on the content of the list
        """
        return self.head is None

    def add_front(self, new_data):
        """
            This inserts a new Node to the front of the 
            linked list
        """
        temp = SLLNode(new_data)
        temp.set_next(self.head)
        self.head = temp

    def add_rear(self, new_data):
        pass

    def size(self):
        """
            Every node of the linked list must be visited
            time complexity is 0(n)
        """
        size = 0
        if self.head is None:
            size = 0
            return size

        current = self.head
        while current is not None:  # while there is more node to read
            size += 1
            current = self.get_next()

        return size

    def search(self, data):
        if self.head is None:
            return "Linked List empty. No nodes to search."

        current = self.head
        while current is not None:
            if current.get_next() == data:
                return True
            else:
                current = current.get_next()

        return False

    def remove(self, data):
        """
            Removes the first ocuurence of a node and returns nothing 
            time complexity is o(n)
        """
        if self.head is None:
            return "Nothing to remove, The linked list is empty."

        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == data:
                found = True
            else:
                if current.get_next() is None:
                    return "Data instance not present."
                else:
                    previous = current
                    current = current.get_next()

        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())


def main():
    sll = SLL()
    sll.add_front("Apple")
    sll.add_front("Mango")
    sll.add_front("Orange")
    sz = sll.is_empty()
    print(sz)

    if __name__ == "__main__":
        main()
