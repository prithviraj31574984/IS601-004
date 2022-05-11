a1 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
a2 = [-1, 1, -2, 2, 3, -3, -4, 5]
a3 = [-0.01, -0.0001, -.15]
a4 = ["-1", "2", "-3", "4", "-5", "5", "-6", "6", "-7", "7"]


def process_array(num, arr):
    print("\nUCID:-pg79\nProcessing Array({}): \n\n".format(num))
    print(arr)
    print(" \n Positive Outputs are:")
    # TODO add new code here to print the desired result
    for x in arr:
        if(int(x)>=0): #to check if x is greater than zero
            print(x,end=" \n")

from datetime import datetime

now = datetime.now() # datetime object containing current date and time
print("now =", now)
dt_string = now.strftime("%d/%m/%Y %H:%M:%S") # dd/mm/YY H:M:S
print("date and time =", dt_string)

print("Problem 3")
process_array(1, a1)
process_array(2, a2)
process_array(3, a3)
process_array(4, a4)
