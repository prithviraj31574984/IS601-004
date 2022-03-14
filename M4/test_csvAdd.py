import csv
from MyCalc import MyCalc

def test_csvmult()
    calc = MyCalc()
    with open("random.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count > 0:
                r =
