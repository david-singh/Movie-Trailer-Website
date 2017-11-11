class Movie():
    """ This Class provides a way to store Movie related information"""
    # constructor  or initializer with arg details of Movie
    def __init__(self, movie_title, storyline, poster_image,
                 trailer_youtube_url):
        self.title = movie_title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube_url
