import csv

filename = input("what file")
with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            r = int(row[0])+int(row[1])
            print(f'{row[0]} * {row[1]} = {row[2]}')
            if r == int(row[2]):
                print("v1 and v2 match")
            else:
                print("value 1 and value2 doo not match")
            line_count += 1
    print(f'Processed {line_count} lines.')
