from main import BooksCollector
class TestBooksCollector:
    def test_add_new_book_positive_valid_name_added(self):
        collector = BooksCollector()
        book_name = "Властелин колец"
        
        collector.add_new_book(book_name)
        
        assert book_name in collector.books_genre
        assert collector.books_genre[book_name] == ""

    def test_set_book_genre_positive_valid_genre_set(self):
        collector = BooksCollector()
        book_name = "Гарри Поттер"
        genre = "Фантастика"
        
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        
        assert collector.get_book_genre(book_name) == genre
    
    def test_get_book_genre_positive_returns_genre(self):
        collector = BooksCollector()
        book_name = "Метро 2033"
        genre = "Фантастика"
        
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        
        result = collector.get_book_genre(book_name)
        assert result == genre

    def test_get_books_genre_positive_returns_dictionary(self):
        collector = BooksCollector()
        
        expected_dict = {
            "Книга 1": "Фантастика",
            "Книга 2": "Комедии"
        }
        
        for name, genre in expected_dict.items():
            collector.add_new_book(name)
            collector.set_book_genre(name, genre)
        
        result = collector.get_books_genre()
        
        assert result == expected_dict

    def test_add_book_in_favorites_positive_book_added(self):
        collector = BooksCollector()
        book_name = "Любимая книга"
        
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        
        favorites = collector.get_list_of_favorites_books()
        assert book_name in favorites
    
    def test_delete_book_from_favorites_positive_book_removed(self):
        collector = BooksCollector()
        book_name = "Любимая книга"
        
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        
        collector.delete_book_from_favorites(book_name)
        
        favorites = collector.get_list_of_favorites_books()
        assert book_name not in favorites

    def test_get_list_of_favorites_books_positive_returns_list(self):
        collector = BooksCollector()
        favorite_books = ["Книга 1", "Книга 2", "Книга 3"]
        
        for book in favorite_books:
            collector.add_new_book(book)
            collector.add_book_in_favorites(book)
        
        result = collector.get_list_of_favorites_books()
        
        assert len(result) == 3
        for book in favorite_books:
            assert book in result

    def test_get_books_for_children_positive_returns_safe_books(self):
        collector = BooksCollector()
        
        books_data = [
            ("Мультик", "Мультфильмы"),  # без рейтинга
            ("Фантастика", "Фантастика"),  # без рейтинга
            ("Страшилка", "Ужасы")  # с рейтингом
        ]
        
        for book, genre in books_data:
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)
        
        children_books = collector.get_books_for_children()
        
        assert "Мультик" in children_books
        assert "Фантастика" in children_books
        assert "Страшилка" not in children_books

    def test_add_new_book_negative_empty_name_not_added(self):
        collector = BooksCollector()
        
        collector.add_new_book("")
        
        assert "" not in collector.books_genre
        assert len(collector.books_genre) == 0

    def test_get_book_genre_negative_nonexistent_book_returns_none(self):
        collector = BooksCollector()
        
        result = collector.get_book_genre("Несуществующая книга")
        
        assert result is None
