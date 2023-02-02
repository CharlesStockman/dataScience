# Declare a Newspaper class. 

# Each Newspaper will have a 'pages' attribute set to an integer and a 'sections' # attribute set to a dictionary.

# The keys in 'sections' will be strings representing a section (i.e. "Politics") and the values will be the starting
# page for that section (i.e. "A5").

# The length of a newspaper should be equal to the number of pages it holds.

# Indexing the newspaper by a section should return the starting # page for that section.

# Make it so two newspapers are considered equal if they have the same number of pages AND the same number of sections

#
# A Tuple to contain the information about each section of a newspaper
#

# EXAMPLE:
monday_sections = {
    "Politics": "A5",
    "Sports": "B2",
    "Entertainment": "C3"
}

tuesday_sections = {
    "Travel": "A5",
    "Cooking": "B2",
}

wednesday_sections = {
    "Classifieds": "A5",
    "Weddings": "B2",
    "Weather": "C3"
}


class Newspaper:
    def __init__(self, pages, sections):
        self.pages = pages
        self.sections = sections

    def __str__(self):
        return f"Newspaper : Pages = {self.pages} and Sections = {self.sections} "

    def __len__(self):
        return self.pages

    def __eq__(self, other):
        result = True if self.pages == other.pages and len(self.sections) == len(other.sections) else False
        return result

    def __getitem__(self, index):
        return self.sections[index]


np1 = Newspaper(pages=80, sections=monday_sections)
np2 = Newspaper(pages=60, sections=tuesday_sections)
np3 = Newspaper(pages=80, sections=wednesday_sections)

print(np1)
print(np2)
print(np3)
print(len(np1))
print(len(np2))
print(np1 == np2)
print(np1 == np3)
print(np1["Politics"])
print(np2["Cooking"])
