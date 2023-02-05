#
# Unit Test the test_if_age file
#

import unittest

# Scenario -- A file that is to be imported has spaces and the spaces cannot be removed.
# The best solution is to execfile, but is different from modules administration since it
# not create a new module
exec(open("loops -- exercise 3.py").read())

class testIfAge(unittest.TestCase):

    def setUp(self):
        self.__age_Dictionary()

    def __age_Dictionary(self):

        '''
            Create a dictionary where:
             key is the age as number 
             value is the classification of the age
        :return: 
        '''
        self.age_dictionary = {}
        for age_as_number in range(0, 2):
            self.age_dictionary[age_as_number] = "baby"

        for age_as_number in range(2, 4):
            self.age_dictionary[age_as_number] = "toddler"

        for age_as_number in range(4, 13):
            self.age_dictionary[age_as_number] = "kid"

        for age_as_number in range(13, 20):
            self.age_dictionary[age_as_number] = "teenager"

        for age_as_number in range(20, 65):
            self.age_dictionary[age_as_number] = "adult"

        for age_as_number in range(65, 121):
            self.age_dictionary[age_as_number] = "elder"

    def test_find_age_original_assignment(self):
        for age in range(0, 121):
            age_from_test_code = self.age_dictionary.get(age)
            age_from_code = find_age_original_assignment(age)
            self.assertEqual(age_from_test_code, age_from_code)

if ( __name__ == '__main__'):
    unittest.main()
