"""
2. write a python program which iterates the integers from 1 to 10
for multipication of three print fixx instead of the number and for the number and instead of the multiple of 5 buzz
for numbers which are multiples of both three and five fizz buzz

"""

def fizz_buzz():
    for i in range(1, 51):
        if i % 15 == 0:
            print("FizzBuzz")
        if i % 3 == 0:
            print("Fizz")
        if i % 5 == 0:
            print("Buzz")
        else:
            print(i)

print(fizz_buzz())