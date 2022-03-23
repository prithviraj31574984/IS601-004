import csv
import math
import operator

# https://stackoverflow.com/a/16503661 using a dict to store values grouped by column names
import statistics
from collections import defaultdict


class MyCalc:
    ans = 0  # todo, class vs static vs instance
    num = 0  # added a dummy for sqrt function
    ops = {'+': operator.add,
           '-': operator.sub,
           '*': operator.mul,
           'x': operator.mul,
           '/': operator.truediv}

    @staticmethod
    def _is_float(val):
        try:
            float(val)
            return True
        except:
            return False

    @staticmethod
    def _is_int(val):
        try:
            int(val)
            return True
        except:
            return False

    @staticmethod
    def _as_number(val):
        if MyCalc._is_int(val):
            return int(val)
        elif MyCalc._is_float(val):
            return float(val)
        else:
            raise Exception("Not a number")

    def calc(self, num1, op, num2):
        # map characters to operator function references
        # https://stackoverflow.com/a/18591880
        # print("num1: " + str(num1))
        # print("num2: " + str(num2))
        if op == "^/":
            num1 = self._as_number(num1)
            self.ans = math.sqrt(num1)
            return self.ans
        else:
            if num1 == "ans":
                return self.calc(self.ans, op, num2)
            else:
                num1 = self._as_number(num1)
                num2 = self._as_number(num2)
                self.ans = MyCalc.ops[op](num1, num2)
                return self.ans
# UCID: pg79    Date: 02/20/2022

class AdvMyCalc(MyCalc):
    def __init__(self):
        super().ops["**"] = operator.pow
        super().ops["//"] = operator.floordiv
        super().ops["%"] = operator.mod


    @staticmethod
    def read_stats_file(input_file):
        # https://stackoverflow.com/a/16503661 split the values of the csv based on columns.
        columns = defaultdict(list)
        with open(input_file, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            line_count = 0
            rows = []
            for row in csv_reader:
                for (k, v) in row.items():
                    columns[k].append(v)
            print(columns)
            return columns

 # UCID: pg79    Date: 02/20/2022
    # Stats calculation method that uses the statistics function and calculates the values for 5 adv functions - Mean, Median, Mode, Standard Deviation and Z-Score
    @staticmethod
    def stats_calc(columns, stats_choice):
        numbers = list(map(float, columns['ï»¿Input|Numbers']))
        if stats_choice == '1':
            mean = statistics.mean(numbers)
            return mean
        elif stats_choice == '2':
            median = statistics.median(numbers)
            return median
        elif stats_choice == '3':
            mode = statistics.mode(numbers)
            return mode
        elif stats_choice == '4':
            std_deviation = statistics.pstdev(numbers)
            return std_deviation
        else:
            mean = statistics.mean(numbers)
            std_deviation = statistics.pstdev(numbers)
            z_score = []
            for num in numbers:
                zs = round((num - mean) / std_deviation, 9)
                z_score.append(zs)
            return z_score

    def squareroot(self, num):
        return math.sqrt(num)

    def square(self, num):
        return operator.pow(num, 2)


if __name__ == '__main__':
    is_running = True
    iSTR = input("Are you ready? Type yes to start or q to quit")
    # calc = MyCalc()
    calc = AdvMyCalc()
    if iSTR == "yes":
        while is_running:
            if iSTR == "quit" or iSTR == "q":
                is_running = False
            else:
                option = input("Enter your option: 1 for equation, 2 for advanced operations. Enter q anytime to quit")
                if option == "quit" or option == "q":
                    print('Thanks for trying out the calculater! Good Bye')
                    is_running = False
                elif option == '1':
                    iSTR = input("What is your eq:")
                    print("Your eq was " + str(iSTR))
                    checks = ["+", "**", "//", "/", "*", "x", "-", "%", "^^",
                              '***']  # added a new symbol for sq root - ^^
                    handled = False                         # UCID: pg79    Date: 02/20/2022
                    for check in checks:
                        if not handled and check in iSTR:
                            nums = iSTR.split(check)
                            print(nums[0])
                            if check == "***":
                                r = calc.square(int(nums[0]))
                            elif check == "^^^":
                                r = calc.squareroot((int(nums[0])))
                            else:
                                r = calc.calc(nums[0].strip(), check, nums[1].strip())
                            print("Result is " + str(r))
                            handled = True
                else:
                    file = "adv_data_file.csv"  # used the file directly instead of input from console for running in pycharm directly.
                    # file = "../stats_numbers.csv"
                    iSTR = input(
                        "Select number for operation: 1 - Mean , 2 - Median, 3- Mode, 4 - Population Standard Deviation, 5 - ZScore")
                    if input == '1' or '2' or '3' or '4' or '5':
                        file_columns = calc.read_stats_file(file)
                        result = calc.stats_calc(file_columns, iSTR)
                    else:
                        print('You have selected an invalid option')
                        handled = False
                    print(f"You have selected {iSTR} and your result is {result}")
                handled = True
            if not handled:
                print("The action you tried is not supported, please try again")
    else:  # exit loop
        print("That is not a valid response. Thanks for trying out the calculater! Good Bye")
        is_running = False
# UCID: pg79    Date: 02/20/2022
