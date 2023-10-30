# # # stacks

"""
    This is known as the last first out data structure 
    example scenario is a stack of pan cakes

    they are recursive data structures. its either empty or recurvive
"""


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """
            This method accepts an item as an input parameter
            and appends it to the end of ou list. this method returns nothing
            The runtime is 0(1) or constant one , because appending to the end of a list happens in constant time.
        """
        self.items.append(item)

    def pop(self):
        """removes and returns last items in a list
            runtime is constant because it removes from
        """
        if self.items:
            return self.items.pop()
        else:
            return None

    def peek(self):
        """
            This returns the last item of the list
            this method runs in constant time
        """
        if self.items:
            return self.items[-1]
        else:
            return None

    def size(self):
        """
            This mehtod returns the len of the list
            The runtime is constant time and runs in constant
            time becase finding the len of the list in constact time
        """
        return len(self.items)

    def is_empty(self):
        """
            Runs in constant time because testing for the
            equality happens in constant time. returns a boolean
            value to show if the list is empy or not
        """
        if self.items:
            return False
        else:
            return True


def main():
    my_stacks = Stack()
    my_stacks.push("Banana")
    my_stacks.push("Mango")
    my_stacks.push("Apple")
    print(my_stacks.size())
    print(my_stacks.is_empty())


if __name__ == "__main__":
    main()
