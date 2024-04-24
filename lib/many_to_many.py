class Author:
    all = []

    def __init__(self, name):
        self.name = name
        self._contracts = []
        type(self).all.append(self)

    def contracts(self):
        return self._contracts.copy()

    def books(self):
        return [contract.book for contract in self._contracts]

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of Book class")
        contract = Contract(self, book, date, royalties)
        self._contracts.append(contract)
        return contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self._contracts)
pass

class Book:
    all = []

    def __init__(self, title):
        self.title = title
        self._authors = []
        self._contracts = []
        type(self).all.append(self)

    def authors(self):
        return self._authors.copy()

    def add_author(self, author):
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of Author class")
        self._authors.append(author)

    def contracts(self):
        return self._contracts.copy()

    def add_contract(self, contract):
        if not isinstance(contract, Contract):
            raise Exception("Contract must be an instance of Contract class")
        self._contracts.append(contract)
pass        


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(date, str):
            raise TypeError("Date must be a string")
        if not isinstance(royalties, int):
            raise TypeError("Royalties must be an integer")
        
        if isinstance(author, Author) and isinstance(book, Book):
            self.author = author
            self.book = book
            self.date = date
            self.royalties = royalties
            type(self).all.append(self)
        else:
            raise TypeError("Invalid types for author and/or book")
pass