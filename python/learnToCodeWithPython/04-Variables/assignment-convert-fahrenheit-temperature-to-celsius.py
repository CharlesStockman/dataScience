# Design a Python Program that ask the user for a temperature in Fahrenheit
# The program should convert the temperature to Celsius and print out a 
# message with the value.  When dealing with any mumeric values in the 
# problem prefer floating point values to integers
#
# Fahrenheit to Celsius Formula --> C = 5 / 9 * ( F - 32 )

fahrenheit = float(input("Please Enter a Fahrenheit Temperature "))
celsius = (5.0 / 9.0) * (fahrenheit - 32)
print("The temperature in Celsius is ", celsius)
