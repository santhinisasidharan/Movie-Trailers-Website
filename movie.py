# This module defines a class 'Movie' and its data members and member functions

import webbrowser

class Movie():
    ''' This class is used for storing data related to a movie'''
    
    def __init__(
                    self, movie_name, movie_storyline,
                    movie_poster, movie_trailer
                    ):
        # Constructor
        
        self.title = movie_name
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer
        
    def show_Trailer(
                        self
                        ):
        #This function opens the movie trailer in browser
        
        webbrowser.open(self.trailer)
