import csv
with open ("Documents\\del.csv") as cv:
    writer=csv.writer(cv)
    writer.writerows("hhh")
cv.close()