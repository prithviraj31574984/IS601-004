a1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a2 = [0, 1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
a3 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
a4 = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]


def process_array(num, arr):
    print("\nUCID:-pg79 \nProcessing Array({}): \n\n".format(num))
    print(arr)
    print("\nOdds output:\n")
    # TODO add necessary print statement to output only the odd values (hint, best if shown as a single line)
    for x in arr:
        if(x%2!=0):  #checking if x odd or even
            print(x)

from datetime import datetime
now = datetime.now() # datetime object containing current date and time
print("now =", now)
dt_string = now.strftime("%d/%m/%Y %H:%M:%S") # dd/mm/YY H:M:S
print("date and time =", dt_string)

print("Problem 1")
process_array(1, a1)
process_array(2, a2)
process_array(3, a3)
process_array(4, a4)
