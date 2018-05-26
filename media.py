class Movie():
    """Class containing details about a movie
    Arg1: String - Movie Title
    Arg2: String - Youtube Url
    Arg3: String - Movie Post Image Url"""
    
    def __init__(self, title, trailer_youtube_url, poster_image_url):
        self.title = title
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = poster_image_url
