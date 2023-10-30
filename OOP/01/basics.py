# # # basic class

class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.pages = pages
        self.price = price
        self.author = author
        # # # prevent other sub classes to modify this attribute
        self.__secret = "This is a secret" 

    def change_title(self, new_title):
        self.title = new_title
        
    def number_of_pages(self):
        return self.pages

    def get_price(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price

    def set_discount(self, amount):
        self._discount = amount

class NewsPaper:
    def __init__(self, day):
        self.day = day

def main():
    b1 = Book("Things fall apart", "Chinua Achebe", 300, 45)
    b2 = Book("Things fall apart", "Chinua Achebe", 300, 45)
    n1 = NewsPaper("Monday")
    print(b1.get_price())

    # # check if they are instances
    print(isinstance(b1, Book))
    print(isinstance(b2, Book))
    print(isinstance(b2, object))
    print(isinstance(n1, object))
    print(isinstance(n1, Book))

if __name__ == '__main__':
    main()
