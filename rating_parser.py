def rating_parser(file_name,delimeter,movie_db,user_db):

   
    rate_data_file = open(file_name)
    
    for line in rate_data_file:
        tokens = line.split(delimeter)
        user_id = tokens[0]
        
        movie_id = tokens[1]
        if user_id in user_db:
            user_db[tokens[0]]["total_movie_watched"] = user_db[tokens[0]]["total_movie_watched"] + 1
        else:
            continue
        if movie_id in movie_db:
            movie_db[tokens[1]]["total_viewers"] = movie_db[tokens[1]]["total_viewers"] + 1
            movie_db[tokens[1]]["total_rating"] = movie_db[tokens[1]]["total_rating"] + int(tokens[2])
        else:
            continue
   
