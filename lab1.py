import csv
import random
from datetime import datetime

random.seed(datetime.now().timestamp())

with open('books.csv') as csv_file:
    table = csv.reader(csv_file, delimiter=';')
    table_list = list(table)

    # 1 exercise
    print("Number of records: ", len(table_list) - 1)

    # 2 exercise
    count = 0
    for row in table_list[1:]:
        if (len(row[1]) > 30):
            count += 1
    print("Number of records with more than 30 characters in the 'Name' field: ", count)

    # 3 exercise (second variant - until 2016)
    author_name = input("Input author details: ")
    print("Книги по запросу " + author_name + ":")
    for row in table_list[1:]:
        if author_name in row[4]:
            time = int(row[6][6:10])
            if (time < 2016):
                print(row[1] + ' ' + row[6][:10])

    # 4 exercise
    with open ("bibliographic references.txt", "w") as file_to_write:
        for i in range(20):
            current_row = random.randrange(1, len(table_list))
            file_to_write.write(str(table_list[current_row][3]) + ". " + str(table_list[current_row][1]) + ' - ' + str(table_list[current_row][6][:10]))
            file_to_write.write('\n')

