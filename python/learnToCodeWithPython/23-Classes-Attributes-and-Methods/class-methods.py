# Define a Chocolate class that accepts and assigns a cacao_content attribute.
class Chocolate:
    def __init__(self, cocoa_content):
        self.cacao_content = cocoa_content

    @classmethod
    def sweet(cls):
        return cls(cocoa_content=30)

    @classmethod
    def semi_sweet(cls):
        return cls(cocoa_content=50)

    @classmethod
    def bitter_sweet(cls):
        return cls(cocoa_content=70)

    @classmethod
    def bitter(cls):
        return cls(cocoa_content=99)


test_class = Chocolate(100)
print("The cocoa content is ", test_class.cacao_content)

# Define a "sweet" class method that returns a Chocolate object with a
# cacao_content value of 30.
sweet = Chocolate.sweet()
print("The cocoa content for sweet is ", sweet.cacao_content)

# Define a "semisweet" class method that returns a Chocolate object with a 
# cacao_content value of 50.
semi_sweet = Chocolate.semi_sweet()
print("The cocoa content for semi-sweet is ", semi_sweet.cacao_content)

# Define a "bitter_sweet" class method that returns a Chocolate object with a 
# cacao_content value of 70.
bitter_sweet = Chocolate.bitter_sweet()
print("The cocoa content for semi-sweet is ", bitter_sweet.cacao_content)

# Define a "bitter" class method that returns a Chocolate object with a 
# cacao_content value of 99.
bitter = Chocolate.bitter()
print("The cocoa content for semi-sweet is ", bitter.cacao_content)
