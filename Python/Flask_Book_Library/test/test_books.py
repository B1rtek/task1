import pytest

from project.books.models import Book


@pytest.mark.parametrize(
    'name',
    [
        'Lalka',
        'Harry Potter i Kamień Filozoficzny',
        'Le Château des Carpathes',
        'W 80 dni dookoła świata'
    ]
)
def test_book_name_good(name):
    book = Book(name, "Someone", 2000, None)
    assert book.name == name

@pytest.mark.parametrize(
    ('name', 'sanitized_name'),
    [
        ('L\'île mystérieuse', 'L&#39;île mystérieuse'),
        ('<script>alert("xss!")</script>', '&lt;script&gt;alert(&#34;xss!&#34;)&lt;/script&gt;'),
        ('Pride & Prejudice', 'Pride &amp; Prejudice')
    ]
)
def test_book_name_bad(name, sanitized_name):
    book = Book(name, "Someone", 2000, None)
    assert book.name == sanitized_name

@pytest.mark.parametrize(
    'author',
    [
        'Bolesław Prus',
        'J. K. Rowling',
        'Jules Vallès',
        'Jan 23'
    ]
)
def test_book_author_good(author):
    book = Book("A book", author, 2000, None)
    assert book.author == author

@pytest.mark.parametrize(
    ('author', 'sanitized_author'),
    [
        ('Howard Allen Frances O\'Brien', 'Howard Allen Frances O&#39;Brien'),
        ('<script alert("xss!") script>', '&lt;script alert(&#34;xss!&#34;) script&gt;'),
        ('Somebody, M.D.C. &c. &c. &c.', 'Somebody, M.D.C. &amp;c. &amp;c. &amp;c.')
    ]
)
def test_book_author_bad(author, sanitized_author):
    book = Book("A book", author, 2000, None)
    assert book.author == sanitized_author
