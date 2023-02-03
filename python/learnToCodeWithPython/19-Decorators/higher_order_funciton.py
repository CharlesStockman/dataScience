# Define an invoke_thrice function.
# It should accept a single argument (which will be a function)
# In its body, the invoke_thrice function should invoke
# the function that's passed in exactly three times.

def invoke_thrice(func):
    for counter in range(3):
        func()

def print_hello_world():
    print("Hello World")

invoke_thrice(print_hello_world)