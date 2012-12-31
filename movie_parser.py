def get_movie_genres(genre_token):
    genre_names = ('unknown','Action','Adventure','Animation','Children','Comedy','Crime','Documentary',
                    'Drama','Fantasy','Film-Noir','Horror','Musical','Mystery','Romance','Sci-Fi','Thriller','War','Western')
    
    genre_list = []    
    i = 5
    for genre in genre_names:
        
        if genre_token[i] == '1' :
            genre_list.append(genre)
        i = i + 1
    
    return genre_list

def movie_parser(file_name,delimeter):

    movie_attributes = ('movieid','title','release_date','videoreleasedate','url')
    
    movies = {}
    f=open(file_name)
    for line in f:
        movie = {}
        tokens = line.split(delimeter)
        i = 0;    
        for attribute in movie_attributes:
            movie[attribute] = tokens[i]
            i = i + 1;
       
        movie["genre"] = get_movie_genres(tokens)
        movie["total_viewers"] = 0
        movie["total_rating"] = 0        
        #print movies
        movies[movie['movieid']] = movie
        
    return movies
