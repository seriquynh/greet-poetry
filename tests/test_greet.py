from greet import hello, hi


def test_hello():
    assert hello("John") == "Hello, John!"


def test_hi():
    assert hi("James") == "Hi, James."
