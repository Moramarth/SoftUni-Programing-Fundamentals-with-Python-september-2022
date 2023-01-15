class Method:

    def __init__(self, string, number):
        self.string = string
        self.number = number

    def __testing__(self, string, number):
        self.string = string
        self.number = number
        result = 0
        if string == "int" and number.isdigit():
            result = int(number) * 2
            return result
        elif string == "real" and is_float(number):
            multiply = float(number) * 1.50
            result = f"{multiply:.2f}"
            return result
        elif string == "string":
            result = f"${number}$"
            return result


def is_float(number):
    try:
        float(number)
        return True
    except ValueError:
        return False


text = input()
num = input()

m1 = Method(text, num)
if m1.__testing__(text, num) is not None:
    print(m1.__testing__(text, num))
