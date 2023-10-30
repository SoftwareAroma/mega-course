# # # Super class

class Publication:
    def __init__(self, title, price):
        self.title = title
        self.price = price


class Periodical(Publication):
    def __init__(self, title, price, period, publisher):
        super().__init__(title, price,)
        self.period = period
        self.publisher = publisher


class Book(Publication):
    def __init__(self, title, author, pages, price):
        super().__init__(title, price)
        self.author = author
        self.pages = pages


class Magazine(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, price, period, publisher)


class NewsPaper(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, publisher, price, period)


def main():
    b1 = Book("Brave New World", "Aldous Huxly", 314, 29.0)
    n1 = NewsPaper("NY Times", 6.0, "New York Times Company", "Daily")
    m1 = Magazine("Scientific America", "Springer Nature", 5.99,"Monthly")

    print(b1.author)
    print(n1.publisher)
    print(b1.price, m1.price, n1.price)


if __name__ == "__main__":
    main()