import csv

# 1
with open('books.csv') as csv_file:
    table = csv.reader(csv_file, delimiter=';')
    table_list = list(table)

    tags = set()
    print("Все тэги: ")
    for row in table_list[1:]:
        tags_array = row[12].split("#")[1:]
        for tag in tags_array:
            tags.add(tag)
    print(tags)

with open('books-en.csv') as csv_file_two:
    table = csv.reader(csv_file_two, delimiter=';')
    table_list = list(table)

    publishers = set()
    print("Все издатели: ")
    for row in table_list[1:]:
        publish_array = row[4].split(";")
        for publisher in publish_array:
            publishers.add(publisher)
    print(publishers)

# 2
print("Самые популярные 20 книг: ")
with open('books.csv') as csv_file:
    table = csv.reader(csv_file, delimiter=';')
    table_list = list(table)
    table_list_names = []
    table_list_amount = []
    most_popular_set = set()
    for row in table_list[1:]:
        table_list_names.append(row[1])
        table_list_amount.append(int(row[8]))
    while (len(most_popular_set) < 20):
        book = max(table_list_amount)
        most_popular_set.add(table_list_names[table_list_amount.index(book)])
        table_list_amount.pop(table_list_amount.index(book))
    print(most_popular_set)

