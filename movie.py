"""
Movie Class

"""


#### ---- MOVIE CLASS ---- ####

class Movie():

    ## -- Init method -- ##

    def __init__(self, title, rating, genre, runtime, three_d, popularity):
        self.title = title
        self.rating = rating
        self.genre = genre
        self.runtime = runtime
        self.three_d = three_d
        self.popularity = popularity

    ## -- __str__ magic method -- ##

    def __str__(self):
        return self.title + " (" + self.rating + ", " + self.genre + ", " + str(self.runtime) + " minutes)"
