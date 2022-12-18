from index import say_hello, root

def test_root():
    assert root() == {"message": "Hello World"}
def test_say_hello():
    assert say_hello("World") == {"message": "Hello World"}