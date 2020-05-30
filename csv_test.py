import csv
with open('C:\Users\user\Desktop\TEMPerGold\1.csv', newline='') as csvfile:
    read = csv.reader(csvfile)
    for row in read:
        print(row)