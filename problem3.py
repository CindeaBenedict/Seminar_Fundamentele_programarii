"""
Write a program that reads temperatures in  celsius from the user untill they enter q
and then prints
all entered temperatures
the avreage, the minimum, macximum and the median temperature
a new list with the values converted to fahrenheit
"""



def temperatures():
    temperatures_list = []
    while True:
        aux =  input("Enter a temperature in Celcisus or q if you have ended the list: ")
        if aux =="q":
            break
        temperatures_list.append(int(aux))
    print("The average: ", sum(temperatures_list)/len(temperatures_list))
    print("The minimum: ", min(temperatures_list))
    print("The maximum: ", max(temperatures_list))
    temperatures_list.sort()
    n = len(temperatures_list)
    if n%2==0:
        median = temperatures_list[int(n//2)] + temperatures_list[int(n//2)-1]/2
    else:
        median = temperatures_list[int(n//2)]
    print("The median temperature: ", median)
    for temp in temperatures_list:
        fahrenheit = (temp*9/5)+32
        print("The fahrenheit: ", fahrenheit)
        fahrenheit = 0


temperatures()