class BookDB:
    books = [{"id": 1, "name": "A Game of Thrones", "author": "George Raymond Richard Martin", "genre": "Fantasy"}]

    def get_all(self):
        return self.books

    def retrieve(self, id):
        try:
            book_id = int(id)
            for book in self.books:
                if book["id"] == book_id:
                    result = book
                else:
                    result = ('Sad', 400)

        except Exception:
            result = ("Incorrect data, check the correctness of the entered data", 400)
            return result

    def add(self, name, author, genre, id):
        exist = False

        for book in self.books:
            if id == book['id']:
                exist = True

        if not exist:
            book = {
                "name": name,
                "author": author,
                "genre": genre,
                "id": self.books[-1]['id'] + 1
            }
            self.books.append(book)
            return book

    def update(self, name, author, genre, id=int):
        for book in self.books:
            if book["id"] == id:
                book["author"] = author
                book["genre"] = genre
                book['name'] = name
                return book
        return "Incorrect data, check the correctness of the entered data", 400

    def delete(self, id):
        self.books = [book for book in self.books if book["id"] != id]