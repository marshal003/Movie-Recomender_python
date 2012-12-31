def user_parser(file_name,delimeter):
    #1|24|M|technician|85711
    user_attributes = ('userid','age','gender','work','zip')
    
    users = {}
    user_data_file = open(file_name)
    for line in user_data_file:
        user = {}
        tokens = line.split(delimeter)
        i = 0;    
        for attribute in user_attributes:
            user[attribute] = tokens[i]
            i = i + 1;
        
        user["total_movie_watched"] = 0
        users[user['userid']] = user
   
    return users
