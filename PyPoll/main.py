#dependencies
import csv
import os
#load files
election_data = os.path.join('Resources', 'election_data.csv')

# Open the file
data=[]
with open(election_data, 'r') as file:
    # Read the file
    reader = csv.DictReader(file)
    for row in reader:
        data.append(row)
#analysis
candidates={}
total=0
for row in data:
    candidate=row['Candidate']
    if candidate not in candidates:
        candidates[candidate]=1
    else:
        candidates[candidate]+=1
    total+=1
winner=max(candidates,key=candidates.get)
analysis=(
f'Election Results\n'
f'-------------------------\n'
f'Total Votes: {total}\n'
f'-------------------------\n'
f'Charles Casper Stockham: {round(((candidates["Charles Casper Stockham"]/total)*100),3)}% ({candidates["Charles Casper Stockham"]})\n'
f'Diana DeGette: {round(((candidates["Diana DeGette"]/total)*100),3)}% ({candidates["Diana DeGette"]})\n'
f'Raymon Anthony Doane: {round(((candidates["Raymon Anthony Doane"]/total)*100),3)}% ({candidates["Raymon Anthony Doane"]})\n'
f'-------------------------\n'
f'Winner: {winner}\n'
f'-------------------------\n'
)
print(analysis)
output = os.path.join("Analysis", "election_analysis.txt")
with open(output, "w") as x:
    x.write(analysis)
