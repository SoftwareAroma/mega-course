# try out the Python stack functions

# TODO: create a new empty stack
class Stack:
    def __init__(self):
        self.list = []

# TODO: push items onto the stack
    def push(self, value):
        self.list.append(value)


# TODO: pop an item off the stack

    def pop(self):
        if self.list:
            self.list.pop()
        else:
            return


def main():
    myList = Stack()
    myList.push("Orange")
    myList.push("Mango")
    myList.push("Berry")
    myList.push("Apple")
    # TODO: print the stack contents
    print(myList.list)

    # TODO: remove items from the list
    myList.pop()
    print(myList.list)


if __name__ == "__main__":
    main()
