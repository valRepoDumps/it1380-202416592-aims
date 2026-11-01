def search_by_title(cart, title):
    wanted = title.casefold()
    for item in cart.items:
        if item.title.casefold() == wanted:
            return item
    return None