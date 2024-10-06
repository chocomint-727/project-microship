import csv

dataset = open('Data/command_line_testing_subset.csv', newline='')

dataset_read = csv.reader(dataset)



def get_score(title):
    ''' This function returns the score as found in the database based on the name of a show '''
    for row in dataset_read:
        if row[1] == title:
            print(row[2])
            return row[2]
   
def filter_by_genres(genres):
    """ This function returns a list of ids that match all specified genres """
    return_rows = [] # collections of rows to return
    for row in dataset_read:
        genres_match = [0] * len(genres) # bitmap for matched genres
        for i, genre in enumerate(genres):
            if genre.lower() in row[3].lower():
                genres_match[i] = 1 # if match, set to 1
                
        if sum(genres_match) == len(genres_match): # if all genres are matched
            return_rows.append(int(row[0]))
            
    return return_rows