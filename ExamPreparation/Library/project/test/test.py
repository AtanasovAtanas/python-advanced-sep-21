from project.library import Library

from unittest import TestCase, main


class Test(TestCase):
    def setUp(self) -> None:
        self.library = Library('Library')

    def test_library_raises_error_when_empty_string_is_passed(self):
        with self.assertRaises(ValueError) as context:
            library = Library('')

        self.assertEqual('Name cannot be empty string!', str(context.exception))

    def test_library_initialization(self):
        self.assertEqual('Library', self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_add_book_should_add_author_and_title(self):
        author = 'Author'
        first_title = 'Title1'
        second_title = 'Title2'
        self.library.add_book(author, first_title)
        self.library.add_book(author, first_title)
        self.library.add_book(author, second_title)

        self.assertEqual(1, len(self.library.books_by_authors))
        self.assertTrue(author in self.library.books_by_authors)
        self.assertEqual([first_title, second_title], self.library.books_by_authors[author])

    def test_add_reader_should_add_the_reader(self):
        reader_name = 'Reader'
        self.library.add_reader(reader_name)

        self.assertEqual(1, len(self.library.readers))
        self.assertTrue(reader_name in self.library.readers)
        self.assertEqual([], self.library.readers[reader_name])

    def test_add_reader_should_return_error_message_when_reader_is_already_registered(self):
        reader_name = 'Reader'
        self.library.add_reader(reader_name)
        result = self.library.add_reader(reader_name)

        self.assertEqual(f"{reader_name} is already registered in the {self.library.name} library.", result)

    def test_rent_book_should_return_error_message_when_reader_is_not_registered(self):
        reader_name = 'reader'
        result = self.library.rent_book(reader_name, 'author', 'title')
        self.assertEqual(f"{reader_name} is not registered in the {self.library.name} Library.", result)

    def test_rent_book_should_return_error_message_when_author_is_not_registered(self):
        reader_name = 'reader'
        author_name = 'author'
        self.library.add_reader(reader_name)

        result = self.library.rent_book(reader_name, author_name, 'title')
        self.assertEqual(f"{self.library.name} Library does not have any {author_name}'s books.", result)

    def test_rent_book_should_return_error_message_when_title_is_not_registered(self):
        reader_name = 'reader'
        author_name = 'author'
        invalid_title = 'title'
        self.library.add_reader(reader_name)
        self.library.add_book(author_name, 'random title')

        result = self.library.rent_book(reader_name, author_name, invalid_title)
        self.assertEqual(f"""{self.library.name} Library does not have {author_name}'s "{invalid_title}".""", result)

    def test_rent_book_should_properly_rent_book(self):
        reader_name = 'reader'
        author_name = 'author'
        first_title = 'title1'
        second_title = 'title2'
        self.library.add_reader(reader_name)
        self.library.add_book(author_name, first_title)
        self.library.add_book(author_name, second_title)

        self.library.rent_book(reader_name, author_name, first_title)

        self.assertEqual([{author_name: first_title}], self.library.readers[reader_name])
        self.assertEqual(1, len(self.library.books_by_authors[author_name]))
        self.assertTrue(first_title not in self.library.books_by_authors[author_name])
        self.assertTrue(second_title in self.library.books_by_authors[author_name])


if __name__ == '__main__':
    main()
