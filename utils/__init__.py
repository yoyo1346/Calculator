import json
import Arithmetics
import json


# OPERANDS = OrderedDict({'^': numpy.power, '*': numpy.multiply, '/': numpy.divide, '+': numpy.add, '-': numpy.subtract})
OPERANDS = []


class Operand:

    def __init__(self, sign: str, strength: int,  func_to_perform: str):
        self.sign = sign
        self.func_to_perform = eval(func_to_perform)
        self.strength = strength
        # self.insert_sorted()

        # OPERANDS.append(self)
        # self.OPERANDS = sorted(self.OPERANDS, key=lambda d: d['Strength'])

    def insert_sorted(self):
        if len(self.OPERANDS) == 0:
            self.OPERANDS.append(self)
            return
        for index, operand in self.OPERANDS:
            if operand.strength > self.strength:
                self.OPERANDS.insert(index, self)


def extract_json(filename: str):
    with open(filename, 'r') as config_file:
        config_dict = json.load(config_file)
    print(config_dict)
    return sorted(config_dict['operands'], key=lambda d: d['strength'])
    # Operand(operand['sign'], operand['strength'], operand['function_to_perform'])


def main():
    print(extract_json('../config.json'))
    # print(OPERANDS)


if __name__ == '__main__':
    main()
