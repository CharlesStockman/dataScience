# Define a fancy_cleanup function that accepts a single string argument  The function should clean up the whitespace
# on both sides of the argument. It should also replace every occurrence of the letter "g" with the letter "z" and
# every occurrence of a space with an exclamation point (!).
#
# fancy_cleanup("       geronimo crikey  ") => "zeronimo!crikey"
# fancy_cleanup("       nonsense  ") => "nonsense"
# fancy_cleanup("grade") => "zrade"

def fancy_cleanup(input_string: str) -> None:
    def string_cleanup(string: str) -> str:
        result = string.strip().replace("g", "z")
        return result

    print("Cleaning the following string:", input_string, "result:", string_cleanup(input_string))


fancy_cleanup("       geronimo crikey  ")
fancy_cleanup("       nonsense  ")
fancy_cleanup("grade")
