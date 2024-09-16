"""
Screen Class

"""


#### ---- SCREEN CLASS ---- ####

class Screen():

    ## -- Init method -- ##

    def __init__(self, number, capacity, three_d):
        self.number = number
        self.capacity = capacity
        self.three_d = three_d

    ## -- __str__ magic method -- ##

    def __str__(self):
        return "Screen " + str(self.number)
