# Calculator

class SimpleCalculator:

    @staticmethod
    def add(first_num, second_num):
        return first_num + second_num

    @staticmethod
    def subtract(first_num, second_num):
        return first_num - second_num

    @staticmethod
    def multiply(first_num, second_num):
        return first_num * second_num

    @staticmethod
    def divide(first_num, second_num):
        return first_num / second_num


calculator = SimpleCalculator()


# Test code
print(calculator.add(4, 5))
print(calculator.subtract(4, 5))
print(calculator.multiply(4, 5))
print(calculator.divide(4, 5))
