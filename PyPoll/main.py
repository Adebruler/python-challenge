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

most_votes=0
for keys in candict:
    candict[keys][1] = candict[keys][0] / votes
    if candict[keys][0] > most_votes:
        most_votes=candict[keys][0]
        winner=keys

# Print data into text file
file=open('ElectionResults.txt',"w")
file.write("Election Results")
file.write('\n'+"-------------------------")
file.write('\n'+f"Total Votes: {votes}")
file.write('\n'+"-------------------------")
for keys in candict:
    file.write('\n'+f"{keys}: {candict[keys][1]*100:.3f}% ({candict[keys][0]})")
file.write('\n'+"-------------------------")
file.write('\n'+f"Winner: {winner}")
file.write('\n'+"-------------------------")
# Print Text File into Terminal
file=open('ElectionResults.txt',"r")
print(file.read())
