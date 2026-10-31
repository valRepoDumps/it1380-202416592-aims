def search_by_title(cart, title):
    for item in cart.items:
        if item == title:
            return item
    return None