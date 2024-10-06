import csv


dataset = open('../Data/anime.csv', newline='')

dataset_read = csv.reader(dataset)

col_titles = dataset_read[0]

for row in dataset_read:
    print(row)
