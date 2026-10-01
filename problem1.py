# This is a sample Python script.

# Press ⌃F5 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
#1. given 2 integers a and b, return true id one of them is 10 or if their sum is 10
def function10(a:int, b:int)->bool:
    if a == 10 or b == 10 or a+b == 10:
        return True
    else:
        return False

a = int(input())
b = int(input())
print(function10(a,b))