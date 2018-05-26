from media import Movie
from fresh_tomatoes import open_movies_page





def generateMoviePage():
    """Generates a webpage based on movie data supplied within the function."""

    #Make empty list for movies"
    movies_list = []  

    #Create a class for each movie 
    avatar = Movie("Avatar The Last Airbender",
                "https://www.youtube.com/watch?v=ZMoGFeMmhKA",
                "https://vignette.wikia.nocookie.net/avatar/images/d/d5/Film_-_The_Last_Airbender_Poster_1.png/revision/latest?cb=20140628064453",
                )
    pacific_rim = Movie("Pacific Rim",
                    "https://www.youtube.com/watch?v=5guMumPFBag",
                    "http://www.impawards.com/2013/posters/pacific_rim_ver4.jpg",
                    )           
    strawinsky = Movie("Strawinsky and the Mysterious House ",
                    "https://www.youtube.com/watch?v=rVGqkwqAhbQ",
                    "https://ia.media-imdb.com/images/M/MV5BZDA1Mzk3NmQtMjExNi00MGRjLWE0NWItNDg3MDlkZTgwMmE4XkEyXkFqcGdeQXVyNTM3MDMyMDQ@._V1_.jpg", 
                    )
    hotwheels = Movie("Hot Wheels Highway 35 World Race",
                    "https://www.youtube.com/watch?v=mHAf2Zk1D38",
                    "https://ia.media-imdb.com/images/M/MV5BMTQ4NTExNzI4M15BMl5BanBnXkFtZTcwMDAwMzQyMQ@@._V1_UY268_CR2,0,182,268_AL_.jpg"
                    )
    
    #Append all of the movie classes into list
    movies_list.append(avatar)
    movies_list.append(pacific_rim)
    movies_list.append(strawinsky)
    movies_list.append(hotwheels)

    #Pass the list into the open_movies_function to generate the webpage
    open_movies_page(movies_list)

if __name__ == "__main__":
    main()
    
