# Define a truthy_or_falsy function that accepts a single argument. The function should return a string that reads
# "The value _____ is ______" where the first space is the argument and the second space is either truthy or falsy.
# 
# truthy_or_falsy(0) => "The value 0 is falsy"
# truthy_or_falsy(5) => "The value 5 is truthy"
# truthy_or_falsy("Hello") => "The value Hello is truthy"
# truthy_or_falsy("") => "The value  is falsy

def algorithm(algorithm_any_argument) -> None:
    def truthy_or_falsy(any_argument) -> str:
        result = "falsy"
        if bool(any_argument):
            result = "truthy"
        return result

    print("The value of", str(algorithm_any_argument).strip(), " is ", truthy_or_falsy(algorithm_any_argument))

algorithm(0)
algorithm(5)
algorithm("Hello")
algorithm("")

