#!/usr/bin/env python

from user import User

import random



class Teacher(User):
    def __init__(self, first_name, last_name) -> None:
        super().__init__(first_name, last_name)
        self.knowledge =  [
            "str is a data type in Python",
            "programming is hard, but it's worth it",
            "JavaScript async web request",
            "Python function call definition",
            "object-oriented teacher instance",
            "programming computers hacking learning terminal",
            "pipenv install pipenv shell",
            "pytest -x flag to fail fast",
        ]

    def teach(self):
         # Check if the knowledge list is not empty
        if self.knowledge:
            # Generate a random index within the range of the knowledge list
            random_index = random.randint(0, len(self.knowledge) - 1)
            # Return the random element from knowledge
            return self.knowledge[random_index]
        else:
            return "I have no knowledge to share."
        pass