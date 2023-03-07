def shop_from_grocery_list(*args):
    budget = int(args[0])
    needed = args[1]
    rest = args[2:]
    bought = []
    remaining = []
    for key, value in rest:
        if key in needed and key not in bought:
            if budget < value:
                break
            bought.append(key)
            budget -= value

    for element in needed:
        if element not in bought:
            remaining.append(element)
    if remaining:
        return f"You did not buy all the products. Missing products: {', '.join(remaining)}."
    return f"Shopping is successful. Remaining budget: {budget:.2f}."



print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))







