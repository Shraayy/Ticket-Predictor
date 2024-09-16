"""
Customer Class
"""

import random


#### ---- CUSTOMER CLASS ---- ####

class Customer():

    ## -- Init method -- ##

    def __init__(self):
        self.age = random.randint(5, 85)
        self.genres_liked = ["Comedy", "Adventure", "Drama"]
        self.genres_liked.remove(random.choice(self.genres_liked))
