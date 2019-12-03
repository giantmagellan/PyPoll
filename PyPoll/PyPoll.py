# Script to analyze voting data
import os
import csv

VOTE_PATH = os.path.join('c:/Users/User/Documents/Homework Data/election_data.csv')
print(VOTE_PATH)

# reading election data csv file
with open(VOTE_PATH, newline='') as votefile:
    votereader = csv.reader(votefile, delimiter=',')
    #print(votereader) # for testing
    header = next(votefile, None) # skips header row
    total_votes = 0
    candidates = []
    for row in votereader:
        total_votes += 1
        candidates.append(row[2])
print("Total Votes:", total_votes)
# print("List of Candidates:", candidates)

# converted row or candidates from csv file to list to find unique values aka list of candidates
CANDIDATES = list(set(candidates))
print(CANDIDATES)

# function to find the number and percentage of the votes each candidate received
def VOTES():
    Li_count = 0
    tooley_count = 0
    khan_count = 0
    correy_count = 0
    totals = len(candidates)
    percentages = []
    each_votes = []
    for i in candidates:
        if i == "Li":
            Li_count += 1 # adds each vote for Li to Li_count
            if Li_count < totals: # finds percentage of votes for Li
                Li_perc = Li_count / totals
        elif i == "O'Tooley":
            tooley_count += 1 # adds each vote for O'Tooley
            if tooley_count < totals: # finds % of votes for O'Tooley
                tooley_perc = tooley_count / totals
        elif i == "Khan":
            khan_count += 1 # adds each vote for khan
            if khan_count < totals: # % of votes for Khan
                khan_perc = khan_count / totals
        else:
            correy_count += 1 # adds each vote for correy
            if correy_count < totals: # % of votes for correy
                correy_perc = correy_count / totals

    # outputs final election data results
    print(f"""
        Election Results
        -----------------------------------------------------------
        Li: {round(Li_perc*100, 2)}%, {Li_count} votes
        O'Tooley: {round(tooley_perc*100, 2)}% {tooley_count} votes
        Khan: {round(khan_perc*100, 2)}% {khan_count} votes
        Correy: {round(correy_perc*100, 2)}% {correy_count} votes
        -----------------------------------------------------------
        Winner: Khan
        """)
VOTES()





