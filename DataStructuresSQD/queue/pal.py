class Deque:
    def __init__(self):
        self.items = []

    def add_rear(self, item):
        self.items.append(item)

    def remove_rear(self):
        if self.items:
            return self.items.pop()
        return None

    def remove_front(self):
        if self.items:
            return self.items.pop(0)
        return None

    def size(self):
        return len(self.items)


def check_palindrome(input_string):
    input_string = input_string.lower()
    my_d = Deque()
    for char in input_string:
        my_d.add_rear(char)

    while my_d.size() >= 2:
        front_item = my_d.remove_front()
        rear_item = my_d.remove_rear()

        if front_item != rear_item:
            return False

    return True


def main():
    one = check_palindrome("racecar")
    two = check_palindrome("oranges")
    three = check_palindrome("kayak")
    four = check_palindrome("mom")
    print(one)
    print(two)
    print(three)
    print(four)


if __name__ == "__main__":
    main()
