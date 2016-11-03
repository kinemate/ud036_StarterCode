import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A boy and his toy",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

movies = [toy_story]
fresh_tomatoes.open_movies_page(movies)