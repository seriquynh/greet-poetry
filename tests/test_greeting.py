from hello_quinx import Person, hello, hi, whatsup, goodbye


def test_hello():
    assert hello(Person("John")) == "Hello, John!"

def test_hi():
    assert hi(Person("Jane")) == "Hi, Jane!"

def test_whatsup():
    assert whatsup(Person("James")) == "What's up? James"

def test_goodbye():
    assert goodbye() == 'Good bye! See you later.'
