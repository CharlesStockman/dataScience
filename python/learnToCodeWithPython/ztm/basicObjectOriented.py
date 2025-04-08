

#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"name = {self.name}, age = {self.age}"

    def get_age(self):
        return self.age


# 1 Instantiate the Cat object with 3 cats
cat_list = [] 
cat_list.append(Cat('Alice', 25))
cat_list.append(Cat('Bob', 20))
cat_list.append(Cat('Chuck', 25))

print("checking the results: ", repr(cat_list))



# 2 Create a function that finds the oldest cat
def find_oldest_cat(cat_list):
  
    oldest_cat = cat_list[0]
    for cat in cat_list[1:]:
        if cat.get_age() > oldest_cat.get_age(): 
            oldest_cat = cat
    return oldest_cat


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f"The oldest cat is {find_oldest_cat(cat_list)} years old.")
