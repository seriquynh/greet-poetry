from hello.core import hello, goodbye


def test_hello():
    assert hello("John") == "Hello, John!"

def test_goodbye():
    assert goodbye() == 'Good bye! See you later.'
