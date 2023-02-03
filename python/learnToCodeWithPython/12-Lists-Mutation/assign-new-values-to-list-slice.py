# Given the tech_companies list below, overwrite the Microsoft, Blueberry, and with the strings “Facebook” and
# “Apple”. Use list slicing syntax.
tech_companies = ["Google", "Microsoft", "Blackberry", "IBM", "Yahoo"]
tech_companies[1:3] = ["Facebook", "Apple"]
print("Overwriting the tech companies using a slice: ", tech_companies)