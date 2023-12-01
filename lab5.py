from enum import Enum
import random
from datetime import datetime

class Movie:
    def __init__(self, id, title, ranking, character_number, ticket_price, genre, comment ,year, month, day):
        self.id = id
        self.title = title
        self.ranking = ranking
        self.character_number = character_number
        self.ticket_price = ticket_price
        self.comment = comment
        self.__genre = genre
        self.__date = datetime(year, month, day)
        
    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, genre):
        self.__genre = genre
    @property
    def date(self):
        return self.__date

    @date.setter
    def date_(self, date):
        self.__date = date    

class Genre(Enum):
    ACTION = 1
    COMEDY = 2
    DRAMA = 3
    FANTASY = 4

class Cinema:
    def __init__(self, name, location,  *movies):
        self.name = name
        self.location = location
        self.movies = list(movies)
       
    @property
    def cinema_date(self):
        return self._date

    @cinema_date.setter
    def cinema_date(self, date):
        self._date = date

    def calculate_profit(self, day):
        for movie in self.movies:
            all_profit = random.randint(1,1000)
            if movie.date == day:
                sold_tickets = random.randint(1,1000) 
                all_profit =+( sold_tickets * movie.ticket_price)
            return all_profit

    def sort_by_date(self):
        self.movies.sort(key=lambda x: x.date, reverse=True)
        
if __name__ == '__main__':
    movie1 = Movie(123456789, "fiting club", 1, 15, 120, Genre.ACTION, "вам ім'я ібрагім а чомнібуть говоріт????", 2006, 6, 3)
    movie2 = Movie(123456789, "Godfather ", 1, 15, 130, Genre.DRAMA, "вам ім'я ібрагім а чомнібуть говоріт????", 2004, 6, 3)
    movie3 = Movie(123456789, "spider man ", 1, 15, 10, Genre.FANTASY, "вам ім'я ібрагім а чомнібуть говоріт????", 2002, 6, 3)
    tarantino = Cinema("tarantino", "drohobuch", movie1,movie2,movie3)
    print(movie2.character_number)
    print(movie1.genre)
    tarantino.sort_by_date()
    for movie in tarantino.movies:
        print(movie.title, movie.date)
    print(tarantino.calculate_profit(3))  
