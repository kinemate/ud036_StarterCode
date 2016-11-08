import media #data structures for medias
import fresh_tomatoes #constructor for the html code

#sample movies using media.Movie class

toy_story = media.Movie("Toy Story",
                        "A boy and his toy",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

zootopia = media.Movie("Zootopia",
                        "Buddy cop comedy adventure",
                        "https://upload.wikimedia.org/wikipedia/en/e/ea/Zootopia.jpg",
                        "https://www.youtube.com/watch?v=jWM0ct-OLsM")

captain_america_civilwar = media.Movie("Captain America: Civil war",
                        "Superhero movie",
                        "https://upload.wikimedia.org/wikipedia/en/5/53/Captain_America_Civil_War_poster.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

#create list containing all movies
movies = [toy_story, zootopia, captain_america_civilwar]
#generate html by handing list to fresh_tomatoes
fresh_tomatoes.open_movies_page(movies)