import webbrowser


class Movie():
    '''The Movie class generates data structure for movie.'''
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        '''
        Args:
        movie_title (str): The movie title
        movie_storyline (str): The movie description
        poster_image (str): The displayed movie poster
        trailer_youtube (str, optional): A clickable movie trailer video
        
        '''
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
