def rectangle(length, width):
    def perimeter():
        return f"Rectangle perimeter: {length * width}"
    def area():
        return f"Rectangle area: {length * 2 + width * 2}"


    if not isinstance(length, int) or not isinstance(width, int):
        return "Enter valid values!"
    return perimeter() + '\n' + area()

