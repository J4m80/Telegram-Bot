def add_item(cart, item):
    cart.append(item)


def remove_item(cart, index):
    if 0 <= index < len(cart):
        return cart.pop(index)
    return None


def clear_cart(cart):
    cart.clear()
