import csv
import os
from typing import Counter

csvpath = "PyPoll/Resources/election_data.csv"
total_votes = 0
winner_of_election = ""


total_candidates = []
total_votes_casted = []
percent_of_candidate = []
prem_results = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    for row in csvreader:
        total_candidates.append(row[2])
        total_votes_casted.append(row[2])
print(f"Total Votes: {len(total_votes_casted)}")

# create dictionary to loop through and tally candidates individually
counter = Counter(total_candidates)
for candidate, frequency in counter.items():
    total_votes = total_votes + frequency

# print each candidate percentage vote and vote tally
for candidate, frequency in counter.items():
    prem_results.append(f"Candidate: {candidate},Percentage: {round(frequency/total_votes,3)*100}%, Frequency: {frequency}")
    print(prem_results)
# print winner with the most votes  
Winner = max(counter, key=counter.get)
print(f"Winner: {Winner}")

# with open('sdf.csv', 'w') as csvfile: 
#     csvwriter = csv.writer(csvfile)
#     for item in prem_results:
#         # csvwriter.writerow(item)
#         print(item)
# Write the result to a text file
PyPollModAssmt = os.path.join("PyPoll/analysis/new.csv")

with open(PyPollModAssmt, 'w') as csvfile: 
    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["---------------------------------------"])
    csvwriter.writerow([f"Total Votes: {total_votes}"])
    csvwriter.writerow(["---------------------------------------"])
    for item in prem_results:
        csvwriter.writerow([f" {item}"])
    csvwriter.writerow(["---------------------------------------"])
    csvwriter.writerow([f"Winner: {Winner}"])
    csvwriter.writerow(["---------------------------------------"])

    