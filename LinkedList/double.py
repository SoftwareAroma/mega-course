# # # this link has one pointer linking the list
# the entry point is the head

class DLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

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
            Replace the next value with a new value
        """
        self.next = new_next

    def get_previous(self):
        """
            returns the previous item in the linked list
        """
        return self.previous

    def set_previous(self, new_previous):
        """
            Replace the next value with a new value
        """
        self.previous = new_previous


def main():
    my_data = DLLNode("Apple")
    print(my_data.get_data())
    new_node = DLLNode("Orange")
    my_data.set_next(new_node)
    print(my_data.get_next())
    prev_node = DLLNode("One")
    my_data.set_previous(prev_node)
    print(my_data.get_previous())


if __name__ == "__main__":
    main()
