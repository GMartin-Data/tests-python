import pytest

from source.contact import Contact


@pytest.fixture
def contact_factory():
    def create_contact(name, age) -> Contact:
        return Contact(name=name, age=age)
    return create_contact


def test_contact_greeting(contact_factory):
    contact = contact_factory("John Doe", 30)
    assert contact.greet() == "Hello, my name is John Doe and I am 30 years old."
