import csv

csv_file_name = '15.02.23/spotify/spotify.cvs'



with open(csv_file_name, 'r', encoding='UTF8') as data_file:
    for row in csv.reader(data_file):
        print(row)