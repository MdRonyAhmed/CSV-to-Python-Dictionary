import csv

mydict = {}
i = 0
head = []
final_list = []
with open('csv-file-to-read-using-python.csv', mode='r') as inp:
    reader = csv.reader(inp)
    for rows in reader:
        if (i == 0):
            head = rows
            i = i +1
        elif (i > 0):
            j = 0
            for value in rows:
                mydict[head[j]] = value
                j = j + 1

            print(mydict)
            final_list.append(mydict)

print(final_list)

            

    