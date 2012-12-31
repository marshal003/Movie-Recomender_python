from movie_parser import movie_parser
from user_parser import user_parser
from rating_parser import rating_parser
from movie_manager import get_most_watched_genre
from movie_manager import get_most_watched_movie
from movie_manager import get_most_active_user
from movie_manager import get_highest_rated_genre
from movie_manager import get_top_movie_by_year



def main():
    movie_db=movie_parser("movie.data","|")
    user_db=user_parser("user.data","|")
    rating_parser("ratings.data","\t",movie_db,user_db)
    
    get_most_active_user(user_db)
    
    #get_most_watched_genre(movie_db)
    
    
    get_most_watched_movie(movie_db)
    
    
    get_highest_rated_genre(movie_db)
    
    get_top_movie_by_year(movie_db)
    
    
if __name__ == '__main__': 
    main()

