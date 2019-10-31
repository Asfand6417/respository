

from math import sqrt


def cube(x):
    return x * x * x


print("Absolute value of the number -1 ", abs(-1))
print("Cube of number 9 is ", cube(9))
print("Squreroot of 81 is ", sqrt(81))





# returning2.py

n = [1, 2, 3, 4, 5]


def stats(x):

    _mx = max(x)
    _mn = min(x)
    _ln = len(x)
    _sm = sum(x)

    return _mx, _mn, _ln, _sm


mx, mn, ln, sm = stats(n)
print(stats(n))

print("Maximum number is  ",mx)
print("Minimum number is ", mn)
print("Number of items are ", ln)
print("Sum of numbers are ", sm)






# redefinition.py

from time import gmtime, strftime


def show_message(msg):
    print(msg)


show_message("Ready.")


def show_message(msg):
    print("Current time is ", strftime("%H:%M:%S", gmtime()))
    print(msg)


show_message("Processing.")





# fun_implicit.py


def power(x, y=1):

    r = 1

    for i in range(y):
        r = r * x

    return r


print(power(3))
print(power(3, 3))
print(power(5, 5))



# fun_keywords.py

def display(name, age, sex):

    print("Name: ", name)
    print("Age: ", age)
    print("Sex: ", sex)


display("Lary", 43, "M")
display("Joan", 24, "F")







# Passing parameters by Reference

# passing_by_reference.py

n = [1, 2, 3, 4, 5]

print("Original list:", n)


def f(x):

    x.pop()
    x.pop()
    x.insert(0, 0)
    print("Inside f():", x)


f(n)

print("After function call:", n)




# Python anonymus function

# lambda_fun.py

y = 6

z = lambda x: x * y
print(z(8))
