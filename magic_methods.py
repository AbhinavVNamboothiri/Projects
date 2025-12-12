class book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"{self.title} by {self.author}, ${self.price}"
    
    def __eq__(self, other):
        return self.price == other.price
    
    def __lt__(self, other):
        return self.price < other.price
    
    def __gt__(self, other):
        return self.price > other.price
    
    def __le__(self, other):
        return self.price <= other.price
    
    def __ge__(self, other):
        return self.price >= other.price
    
    def __ne__(self, other):
        return self.price != other.price
    
    def __add__(self, other):
        return self.price + other.price

    def __sub__(self, other):
        return self.price - other.price

    def __mul__(self, other):
        return self.price * other.price

    def __truediv__(self, other):
        return self.price / other.price

    def __floordiv__(self, other):
        return self.price // other.price

    def __mod__(self, other):
        return self.price % other.price

    def __pow__(self, other):
        return self.price ** other.price

    def __iadd__(self, other):
        self.price += other.price
        return self

    def __isub__(self, other):
        self.price -= other.price
        return self

    def __imul__(self, other):
        self.price *= other.price
        return self

    def __itruediv__(self, other):
        self.price /= other.price
        return self

    def __ifloordiv__(self, other):
        self.price //= other.price
        return self

    def __imod__(self, other):
        self.price %= other.price
        return self

    def __ipow__(self, other):
        self.price **= other.price
        return self
    
    def __contains__(self, other):
        return other in self.title
    
    def __getitem__(self, key):
        return getattr(self, key)

book1 = book("Book 1", "Author 1", 10)
book2 = book("Book 2", "Author 2", 20)
book3 = book("Book 3", "Author 3", 30)

print(book1)
print(book2)
print(book3)

print("Book" in book1)
print("Author" in book2)
print("Price" in book3)

print(book1["title"])
print(book2["author"])
print(book3["price"])

print(book1 == book2)
print(book1 < book2)
print(book1 > book2)
print(book1 <= book2)
print(book1 >= book2)
print(book1 != book2)

print(book1 + book2)
print(book1 - book2)
print(book1 * book2)
print(book1 / book2)
print(book1 // book2)
print(book1 % book2)
print(book1 ** book2)

book1 += book2
print(book1)
book1 -= book2
print(book1)
book1 *= book2
print(book1)
book1 /= book2
print(book1)
book1 //= book2
print(book1)
book1 %= book2
print(book1)
book1 **= book2
print(book1)