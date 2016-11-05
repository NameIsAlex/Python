user_input = 1
while user_input != 0:
    one = int(input("Enter integer."))
    two = int(input("Enter integer."))
    three = int(input("Enter integer."))
    four = int(input("Enter integer."))
    five = int(input("Enter integer."))
    break
list = [one + two + three + four + five]
average = sum(list) / 5
print('The average is', average)
