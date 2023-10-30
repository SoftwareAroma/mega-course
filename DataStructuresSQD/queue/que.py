# adding items == enqueue
# removing items == dequeue
# queue are recursive

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """
            This method insert an element to the start of 
            the list of items, this forces the element one index to the 
            right, the run time is linear or o(1)
        """
        self.items.insert(0, item)

    def dequeue(self):
        """
        This method removes the last item of the list and returns it
        (the fronts item of the list)
        The runtime is constant time, appending o a list happens in constant time
        """
        if self.items:
            return self.items.pop()
        return None

    def peek(self):
        """
            This method returns the next item in the list
            provided the list is not empty. This does not remove anything from the list, return the last item in the list,(frontmost item in the queue)
            This happens in constant time. 0(1)
        """
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        """
            This method return the size of the queue, that is the length of the list
            This happens in constant time. 0(1)
        """
        return len(self.items)

    def is_empty(self):
        """
        This method return true or false depending on the content of the list
        This happens in constant time
        """
        return self.items == []


def main():
    my_q = Queue()
    print(my_q.size())
    print(my_q.is_empty())
    my_q.enqueue("banana")
    my_q.enqueue("apple")
    my_q.enqueue("orange")
    print(my_q.peek())
    print(my_q.items)
    print(my_q.size())
    my_q.dequeue()
    print(my_q.items)


if __name__ == "__main__":
    main()
