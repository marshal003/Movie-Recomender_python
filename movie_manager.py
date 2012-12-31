import pprint

def get_most_active_user(user_db):
    
    movie_watched = 0
    most_active_users = []
    
    for user_id in user_db:
    
        if movie_watched < user_db[user_id]["total_movie_watched"]:
            movie_watched = user_db[user_id]["total_movie_watched"]
            most_active_users = []
            most_active_users.append(user_db[user_id])

        elif movie_watched == user_db[user_id]["total_movie_watched"]:
            
            most_active_users.append(user_db[user_id])
            
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint("Most Active User(s):   ")
    pp.pprint(most_active_users)


def get_most_watched_movie(movie_db):
   
    most_watched_movies = []
    most_watched_count = 0;
    
    for movie_id in movie_db:
        
        if most_watched_count < movie_db[movie_id]["total_viewers"]:
            most_watched_count = movie_db[movie_id]["total_viewers"]
            most_watched_movies = []
            most_watched_movies.append(movie_db[movie_id])
            
        elif most_watched_count == movie_db[movie_id]["total_viewers"]:
        
            most_watched_movies.append(movie_db[movie_id])
    
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint("Most Watched Movie(s)  :   ")
    pp.pprint(most_watched_movies)
    
def get_most_watched_genre(movie_db):
    
    
    genre_names = ('unknown','Action','Adventure','Animation','Children','Comedy','Crime','Documentary',
                    'Drama','Fantasy','Film-Noir','Horror','Musical','Mystery','Romance','Sci-Fi','Thriller','War','Western')
    
    movie_count_genre = {'unknown': 0,'Action':0,'Adventure':0,'Animation':0,'Children':0,'Comedy':0,'Crime':0,'Documentary':0,
                    'Drama':0,'Fantasy':0,'Film-Noir':0,'Horror':0,'Musical':0,'Mystery':0,'Romance':0,'Sci-Fi':0,'Thriller':0,'War':0,'Western':0}
    
    
    for movie in movie_db:
        for genre in movie_db[movie]["genre"]:
            movie_count_genre[genre] = movie_count_genre[genre] + movie_db[movie]["total_viewers"]
             
    max_movie_count = 0    
    most_watched_genre = 0
    for genre in movie_count_genre:
        if(max_movie_count < movie_count_genre[genre]):
            max_movie_count = movie_count_genre[genre]
            most_watched_genre = genre

    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint("Most Watched genre is :   ")
    pp.pprint(most_watched_genre)


def get_highest_rated_genre(movie_db):
    
     genre_rating={}
     for movie in movie_db:
        
        for genre in movie_db[movie]["genre"]:
            
            if genre in genre_rating:
                genre_rating[genre] = genre_rating[genre] + movie_db[movie]["total_rating"]
            else:
                genre_rating[genre]=movie_db[movie]["total_rating"]
                
    #max_genre_rate=0
    max_genre_rate = 0

    highest_rated_genre = []
    for genre in genre_rating:
        if(max_genre_rate < genre_rating[genre]):
        
            max_genre_rate = genre_rating[genre]
            
            highest_rated_genre=[genre]
        elif max_genre_rate == genre_rating[genre]:
            highest_rated_genre.append(genre)
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint("highest rated genre is :   ")
    pp.pprint(highest_rated_genre)

