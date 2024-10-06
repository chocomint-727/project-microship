import csv

dataset = open('/root/team-project-microship/Data/anime.csv', newline='')

dataset_read = csv.reader(dataset)

#for row in dataset_read:
#    print(row)

def get_genre(title):
    for row in dataset_read:
        if row[1] == title:
            print(row[3])
            return row[3]
