import csv


dataset = open('/root/team-project-microship/Data/anime.csv', newline='')

dataset_read = csv.reader(dataset)

scores = []
titles = []
for row in dataset_read:
    titles.append(row[1])

for row in dataset_read:
    scores.append(row[2])

def get_score():
    #

dataset.close()
