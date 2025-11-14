import pytest

from project.customers.models import Customer

@pytest.mark.parametrize(
    'name',
    [
        'Jan Kowalski',
        'Jan Paweł 2'
        'Salomėja Bučinskaitė-Bučienė'
    ]
)
def test_customer_name_good(name):
    customer = Customer(name, "City", 0)
    assert customer.name == name


@pytest.mark.parametrize(
    ('name', 'sanitized_name'),
    [
        ('Lewis\' Carroll', 'Lewis&#39; Carroll'),
        ('<a href="https://google.com">link</a>', '&lt;a href=&#34;https://google.com&#34;&gt;link&lt;/a&gt;'),
        ('Ken Thompson, Dennis Ritchie & Brian Kernighan', 'Ken Thompson, Dennis Ritchie &amp; Brian Kernighan')
    ]
)
def test_customer_name_bad(name, sanitized_name):
    customer = Customer(name, "City", 0)
    assert customer.name == sanitized_name


@pytest.mark.parametrize(
    'city',
    [
        'Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch',
        'Москва',
        'Stanisławów 1.'
    ]
)
def test_customer_city_good(city):
    customer = Customer("Name", city, 0)
    assert customer.city == city

@pytest.mark.parametrize(
    ('city', 'sanitized_city'),
    [
        ('Saint John\'s', 'Saint John&#39;s'),
        ('<a href="https://google.com">link>', '&lt;a href=&#34;https://google.com&#34;&gt;link&gt;'),
        ('Antigua & Barbuda (I know it\'s not a city)', 'Antigua &amp; Barbuda (I know it&#39;s not a city)'),
    ]
)
def test_customer_city_bad(city, sanitized_city):
    customer = Customer("Name", city, 0)
    assert customer.city == sanitized_city