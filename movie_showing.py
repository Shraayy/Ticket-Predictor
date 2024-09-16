"""
Composition
Coding Exercise: Composition
Movie Showing
"""

import random

from customer import Customer


#### ---- MOVIE SHOWING CLASS ---- ####

class MovieShowing:

    ## -- Init method -- ##

    def __init__(self, time, screen, movie):
        self.time = time
        self.screen = screen
        self.movie = movie
        self.watchers = 0

    ## -- Simulate revenue method -- ##

    def simulate(self, total_customers):

        ## -- Simulate each customer -- ##

        for i in range(int(total_customers)):
            customer = Customer()

            ## -- Filter by rating and genre -- ##

            if customer.age < 13 and self.movie.rating == "PG-13":
                continue
            elif customer.age < 17 and self.movie.rating == "R":
                continue
            elif self.movie.genre not in customer.genres_liked:
                continue

            ## -- Determine if customer sees movie -- ##

            else:
                num = (random.randint(0, 100)) / 100
                if self.movie.popularity >= num:
                    self.watchers += 1

        ## -- Check theater capacity -- ##

        if self.watchers > self.screen.capacity:
            self.watchers = self.screen.capacity

        ## -- Print results and return revenue -- ##

        total_revenue = self.watchers * self.cost
        print("The " + str(self.time) + " show of " + str(self.movie.title) + " made $" + str(total_revenue))
        print(str(self.watchers), "customers each paid $" + str(self.cost))
        return total_revenue

    ## -- Cost property getter method -- ##

    @property
    def cost(self):
        price = 10
        time = int(self.time[0])
        if time >= 6:
            price += 2
        if self.movie.three_d and self.screen.three_d:
            price += 3
        return price

    ## -- __lt__ magic method -- ##

    def __lt__(self, other_movie):
        return self.time < other_movie.time

    ## -- __str__ magic method -- ##

    def __str__(self):

        ## -- Build line about showing -- ##

        description = str(self.time) + " " + str(self.movie) + " - "
        if self.movie.three_d and self.screen.three_d:
            description += " (3D) "
        description += str(self.screen) + "," + " $" + str(self.cost)

        ## -- Return line -- ##

        return description
