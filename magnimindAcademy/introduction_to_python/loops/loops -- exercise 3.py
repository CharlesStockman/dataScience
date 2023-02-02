def find_age_original_assignment(age):
    ''' Converts an ags ( integer ) to a description or classifier

    :parameter age -- A person age typed as integer.  Assumption the input is an integer
    :type age : int
    :returns The classification of the input age
    :rtype string ( "baby", "toddler", "teenager", "adult", "elder"

    If the person is less than 2 years old, print a message that the person is a baby.\n
    If the person is at least 2 years old but less than 4, print a message that the person is a toddler.\n
    If the person is at least 4 years old but less than 13, print a message that the person is a kid.\n
    If the person is at least 13 years old but less than 20, print a message that the person is a teenager.\n
    If the person is at least 20 years old but less than 65, print a message that the person is an adult.\n
    If the person is age 65 or older, print a message that the person is an elder.`\n

    :return: 
    '''

    if age < 2:
        result = "baby"
    elif age < 4:
        result = "toddler"
    elif age < 13:
        result = "kid"
    elif age < 20:
        result = "teenager"
    elif age < 65:
        result = "adult"
    else:
        result = "elder"

    return result


def a_functional_if(age):
    ''' An example of an if using function paradigm ( it is contrived )

    :parameter age -- The age of the person.  Assumption the input is an integer
    :type age : int
    :returns None
    :rtype None

    The expression will expect an age and convert that age to string which will be filtered for strings
    "adult" or "elder".  Then the filtered string will be converted to the person the statement
    "is allowed to enter the establishment".
    '''

    def provide_str(data):
        ''' function used by the map command

        :parameter data -- Used to satisfy the interface need for the program to run
        :type data : string
        :returns A single constant string
        :rtype: str
        '''
        return "The person is old enough to enter the establishment"

    # Some Notes
    #   The filter and map return an iterator -- To get all values typecast to a list or usa a loop
    #   Convert a string to a list -- [ <string> ] -- ex. [find_age_original_assignment(age)]
    #           Remember string is an iterator and list("test") will create a string of ['t', 'e', 's', 't']
    result = list(map(provide_str,
                      filter(lambda x: x in ['adult', 'elder'], [find_age_original_assignment(age)])))
    answer = "" if len(result) == 0  else str(list(result)[0])
    print(f"The answer has a length of {len(answer):3d} -- \"{answer}\" ")


if __name__ == "__main__":
    age_as_string = input("Please enter the age of the person: ")
    try:
        age_of_person = int(age_as_string)
        print(f"The person is a(n) {find_age_original_assignment(age_of_person)}")
    except ValueError:
        print(f"Could not convert {age_as_string} to a number ")

    a_functional_if(25)
    a_functional_if(5)
