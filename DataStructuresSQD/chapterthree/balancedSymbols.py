class Stacks:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []


def check_match(content):
    symbols = {
        '[': ']',
        '(': ')',
        '{': '}'
    }

    openers = symbols.keys()
    closures = symbols.values()

    my_list = Stacks()

    index = 0

    while index < len(content):
        symbol = content[index]
        if symbol in openers:
            my_list.push(content[index])
        else:
            if my_list.is_empty():
                return False
            else:
                top_symbol = my_list.pop()
                if symbol != symbols[top_symbol]:
                    return False
        index += 1

    if my_list.is_empty():
        return True
    else:
        return False


if __name__ == "__main__":
    print(check_match('([{}])'))
    print(check_match('(([{}]])'))
