"""
Ticket Predictor

Businesses often use simulations to help predict the effects of different decisions they can make.
Help a movie theater build a simulation to optimize its showing. Use composition to represent a movie
screening as a movie paired with a screen.

"""

import csv
from movie import Movie
from movie_showing import MovieShowing
from screen import Screen


#### ---- LOAD MOVIES FUNCTION ---- ####

def load_movies(filename):
    loaded_movies = []
    with open("./data/movies.csv") as movie_file:
        csvreader = csv.reader(movie_file)
        next(csvreader)
        for row in csvreader:
            title, rating, genre, runtime, three_d, popularity = row
            three_d = three_d == "True"
            runtime = int(runtime)
            popularity = float(popularity)
            loaded_movies.append(Movie(title, rating, genre, runtime, three_d, popularity))
    return loaded_movies


#### ---- LOAD SCREENS FUNCTION ---- ####

def load_screens(filename):
    loaded_screens = []
    with open("./data/screens.csv") as screen_file:
        csvreader = csv.reader(screen_file)
        next(csvreader)
        for row in csvreader:
            number, capacity, three_d = row
            number = int(number)
            capacity = int(capacity)
            three_d = three_d == "True"
            loaded_screens.append(Screen(number, capacity, three_d))
    return loaded_screens


#### ---- LOAD SHOWINGS FUNCTION ---- ####

def load_showings(filename):
    loaded_showings = []
    with open("./data/showings.csv") as showing_file:
        csvreader = csv.reader(showing_file)
        next(csvreader)
        for row in csvreader:
            time, screen_number, movie_name = row
            for screen in screens:
                if screen.number == int(screen_number):
                    break
            for movie in movies:
                if movie.title == movie_name:
                    break
            loaded_showings.append(MovieShowing(time, screen, movie))
    return loaded_showings


#### ---- SETUP ---- ####

movies = load_movies("movies.csv")
screens = load_screens("screens.csv")
showings = load_showings("showings.csv")

## -- Output sorted showings -- ##

showings.sort()
print("TODAY'S SHOWINGS")
for showing in showings:
    print(showing)

## -- Print intro -- ##

total_customers = 400
print("\nToday there are", total_customers, "potential moviegoers at any given time.")
input("\nPress enter to simulate showings...\n")

#### ---- SIMULATION LOOP ---- ####

total_revenue = 0
for showing in showings:
    total_revenue += showing.simulate(total_customers)
    input("Press enter to continue...\n")

## -- Final output -- ##

print("In total, the theater is forecasted to make", "$" + str(total_revenue), "from these showings.")
