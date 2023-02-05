class Poem:

    def __init__(self):
        self.poem = None

    def __load_poem(self):
        """
         loads the string of a poem into a list
       """

        poem_as_string = ''' Deep into that darkness peering,
         Long I stood there, wondering, fearing,
         Doubting, dreaming dreams no mortals
         Ever dared to dream before;
         But the silence was unbroken,
         And the stillness gave no token,
         And the only word there spoken
         Was the whispered word, "Lenore!"
         This I whispered, and an echo
         Murmured back the word, "Lenore!"
         Merely this, and nothing more. '''

        poem_as_list = poem_as_string.split('\n')

        return poem_as_list

    def get_poem(self):
        """
         Return the poem to the user .  Uses lazy initialization
        """
        if self.poem is None:
            self.poem = self.__load_poem()
        return self.poem

    def __str__(self):
        """
         A string to easily identify the instance of the class to the developer
        """
        self.get_poem()
        return f"Class is Poem and there {len(self.poem)} lines"

    def __len__(self):
        '''
            The length of the instance of class is the number of lines in the poem
        '''
        self.get_poem()
        return len(self.poem)
