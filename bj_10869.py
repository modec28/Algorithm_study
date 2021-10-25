input_str = input()

class arithmetic_operation_2args:
    def sum(self, list_integer):
        return sum(list_integer)
    def subtract(self, list_integer):
        return sum([list_integer[0], -list_integer[1]])
    def multiply(self, list_integer):
        return list_integer[0] * list_integer[1]
    def divide_quotient(self, list_integer):
        return int(list_integer[0] / list_integer[1])
    def divide_remainder(self, list_integer):
        return list_integer[0] % list_integer[1]

arithmetic_op = arithmetic_operation_2args()

print(arithmetic_op.sum(list(map(lambda x: int(x), input_str.split()))))
print(arithmetic_op.subtract(list(map(lambda x: int(x), input_str.split()))))
print(arithmetic_op.multiply(list(map(lambda x: int(x), input_str.split()))))
print(arithmetic_op.divide_quotient(list(map(lambda x: int(x), input_str.split()))))
print(arithmetic_op.divide_remainder(list(map(lambda x: int(x), input_str.split()))))
