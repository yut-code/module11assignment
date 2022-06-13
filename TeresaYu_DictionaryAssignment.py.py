# Module 11 Dictionary Assignment
# Teresa Yu

# asking the user to input an integer
number = int(input("Input a number: "))

# dict comprehension syntax: 
# dictionary = {key: value for vars in iterable}
# creates a dict. the key is the element in the iterable aka range and the value is the key squared
# key : key**2 -> what determines the key is the range, which goes from 1 to the inputted number (must be 1, number+1 since range defaults at 0)
dict = {key: key**2 for key in range(1, number+1)}

#print the dict
print(dict)