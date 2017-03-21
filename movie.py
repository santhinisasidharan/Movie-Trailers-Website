import webbrowser
class Movie():
    def __init__(self, movie_name , movie_storyline, movie_poster, movie_trailer):
        self.title = movie_name
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer
    def show_Trailer(self):
        webbrowser.open(self.trailer)
