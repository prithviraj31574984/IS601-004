import csv
from collections import defaultdict

import pytest

from MyCalc import AdvMyCalc
from MyCalc import MyCalc


def read_file_data(calc_function):
    filename = calc_function + ".csv"
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        rows = []
        for row in csv_reader:
            if line_count > 0:
                rows.append(row)
            line_count += 1
        return rows


def read_adv_stats_rows():
    filename = "adv_data_file.csv"
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        rows = []
        for row in csv_reader:
            if line_count > 0:
                rows.append(row)
            line_count += 1
        return rows


def read_adv_stats_file_data():
    filename = "adv_data_file.csv"
    columns = defaultdict(list)
    with open(filename, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        for row in csv_reader:
            for (k, v) in row.items():
                columns[k].append(v)
        return columns


def is_float(val):
    try:
        float(val)
        return True
    except:
        return False


def is_int(val):
    try:
        int(val)
        return True
    except:
        return False


def as_number(val):
    if MyCalc._is_int(val):
        return int(val)
    elif MyCalc._is_float(val):
        return float(val)
    else:
        raise Exception("Not a number")


@pytest.fixture
def ans(request):
    val = request.config.cache.set('ans', 0)
    return val


@pytest.fixture(scope='session')
def init_calc():
    return MyCalc()


@pytest.fixture(scope='session')
def init_adv_calc():
    return AdvMyCalc()


# UCID: pg79    Date: 02/20/2022
# the calculator test data is parameterized and then values from it corresponding to num1 and num2 are send to the add function in calc and then sends a result back. This result is
# compared against the value in the input dict.

@pytest.mark.parametrize("row", read_file_data("add"))
def test_num_add_num(init_calc, row):
    result = init_calc.calc(row[0], "+", row[1])
    print("\n")
    print(result)

    print(row[2])
    if result == as_number(row[2]):
        # Positive check
        print("Positive Test")
        assert result == as_number(row[2])
    else:
        # Negative check
        print("Negative Test")
        assert result != as_number(row[2])


# UCID: pg79    Date: 02/20/2022
@pytest.mark.parametrize("row", read_file_data("sub"))
def test_num_sub_num(init_calc, row):
    result = init_calc.calc(row[0], "-", row[1])
    if result == as_number(row[2]):
        # Positive check
        print("\n")
        print("Positive Test")
        assert result == as_number(row[2])
    else:
        # Negative check
        print("\n")
        print("Negative Test")
        assert result != as_number(row[2])


# UCID: pg79    Date: 02/20/2022
@pytest.mark.parametrize("row", read_file_data("mul"))
def test_num_mul_num(init_calc, row):
    result = init_calc.calc(row[0], "x", row[1])
    if result == as_number(row[2]):
        # Positive check
        print("\n")
        print("Positive Test")
        assert result == as_number(row[2])
    else:
        # Negative check
        print("\n")
        print("Negative Test")
        assert result != as_number(row[2])


# UCID: pg79    Date: 02/20/2022
@pytest.mark.parametrize("row", read_file_data("div"))
def test_num_div_num(init_calc, row):
    result = init_calc.calc(row[0], "/", row[1])
    if result == as_number(row[2]):
        # Positive check
        print("\n")
        print("Positive Test")
        assert result == as_number(row[2])
    else:
        # Negative check
        print("\n")
        print("Negative Test")
        assert result != as_number(row[2])


# UCID: pg79    Date: 02/20/2022
@pytest.mark.parametrize("row", read_file_data("square"))
def test_num_square_num(init_adv_calc, row):
    row[2] = '2'
    result = init_adv_calc.calc(row[0], "**", row[2])
    if result == as_number(row[1]):
        # Positive check
        print("\n")
        print("Positive Test")
        print("Val= " + row[0] + " Result = " + str(result))
        assert result == as_number(row[1])
    else:
        # Negative check
        print("\n")
        print(result)
        print("Negative Test")
        print("Val= " + row[0] + " Result = " + str(result))
        assert result != as_number(row[1])


# UCID: pg79    Date: 02/20/2022
@pytest.mark.parametrize("row", read_file_data("squareroot"))
def test_num_square_root_num(init_adv_calc, row):
    result = init_adv_calc.calc(row[0], "^/", "0")
    if result == as_number(row[1]):
        # Positive check
        print("\n")
        print("Positive Test")
        print("Val= " + row[0] + " Result = " + str(result))
        assert result == as_number(row[1])
    else:
        # Negative check
        print("\n")
        print(result)
        print("Negative Test")
        print("Val= " + row[0] + " Result = " + str(result))
        assert result != as_number(row[1])


# UCID: pg79    Date: 02/20/2022
def test_mean(init_adv_calc):
    data = read_adv_stats_file_data()
    calc_mean = init_adv_calc.stats_calc(data, '1')
    numbers = list(map(float, data['ï»¿Input|Numbers']))
    if calc_mean == as_number(data['Mean|Positive Case'][0]):
        # Positive check
        print("\n")
        print("Positive Test")
        assert calc_mean == as_number(data['Mean|Positive Case'][0])
    else:
        # Negative check
        print("\n")
        print("Negative Test")
        assert calc_mean != as_number(data['Mean|Positive Case'][0])


# UCID: pg79    Date: 02/20/2022
def test_median(init_adv_calc):
    data = read_adv_stats_file_data()
    calc_median = init_adv_calc.stats_calc(data, '2')
    numbers = list(map(float, data['ï»¿Input|Numbers']))
    if calc_median == as_number(data['Median|Positive Case'][0]):
        # Positive check
        print("\n")
        print("Positive Test")
        assert calc_median == as_number(data['Median|Positive Case'][0])
    else:
        # Negative check
        print("\n")
        print("Negative Test")
        assert calc_median != as_number(data['Median|Positive Case'][0])


# UCID: pg79    Date: 02/20/2022
def test_mode(init_adv_calc):
    data = read_adv_stats_file_data()
    calc_mode = init_adv_calc.stats_calc(data, '3')
    numbers = list(map(float, data['ï»¿Input|Numbers']))
    if calc_mode == as_number(data['Mode|Positive Case'][0]):
        # Positive check
        print("\n")
        print("Positive Test")
        assert calc_mode == as_number(data['Mode|Positive Case'][0])
    else:
        # Negative check
        print("\n")
        print("Negative Test")
        assert calc_mode != as_number(data['Mode|Positive Case'][0])


# UCID: pg79    Date: 02/20/2022
def test_std_deviation(init_adv_calc):
    data = read_adv_stats_file_data()
    calc_std_deviation = round(init_adv_calc.stats_calc(data, '4'), 9)
    print(calc_std_deviation)
    if calc_std_deviation == as_number(data['Pop Std Deviation|Positive Case'][0]):
        # Positive check
        print("\n")
        print("Positive Test")
        assert calc_std_deviation == as_number(data['Pop Std Deviation|Positive Case'][0])
    else:
        # Negative check
        print("\n")
        print("Negative Test")
        assert calc_std_deviation != as_number(data['Pop Std Deviation|Positive Case'][0])


# UCID: pg79    Date: 02/20/2022
# testing all values in one array since the data set is predefined and picking the data by columns instead of rows. The common stats_calc function
# is used for all 5 calculations so the z score is also calculated at one go
def test_z_score(init_adv_calc):
    data = read_adv_stats_file_data()
    calc_z_score = init_adv_calc.stats_calc(data, '5')
    z_score_test_values = list(map(float, data['Positive Case|Z-Score']))
    print(calc_z_score)
    # print(z_score_test_values)
    if calc_z_score == z_score_test_values:
        print(calc_z_score)
        print("Positive Test Case")
        assert calc_z_score == z_score_test_values
    else:
        print(calc_z_score)
        print("Negative Test Case")
        assert calc_z_score != z_score_test_values
