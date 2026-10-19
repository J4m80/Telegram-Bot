from queue import Empty

from cart import add_item, remove_item, clear_cart


def test_add_item():
    cart = []
    add_item(cart, "Pizza")
    assert cart == ["Pizza"]

def test_remove_cart():
    cart = ["Pizza", "Burger"]
    remove_item(cart, 5)
    assert cart == ["Pizza", "Burger"]

def test_remove_invalid_index():
    cart = ["Pizza"]
    result = remove_item(cart, 5)
    assert result is None
    assert cart == ["Pizza"]

def test_clear_cart():
    cart = ["Pizza", "Burger", "French fries"]
    clear_cart(cart)
    assert cart == []
