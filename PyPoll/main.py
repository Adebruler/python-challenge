import os
import csv


with open('election_data.csv', newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    votes=0
    candict={}

    csv_header = next(csvreader,None)

    for row in csvreader:
        votes += 1
        cand = row[2]
        if cand in candict.keys():
            candict[cand][0] += 1
        else:
            candict[cand] = [1,float(1)]
for keys in candict:
    candict[keys][1] = candict[keys][0] / votes

print(votes)
print(candict)
# print(candlist)
