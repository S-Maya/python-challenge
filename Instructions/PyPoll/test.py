def show_line():
    print(f"-"*30)

# importing library
import os
import csv

# csv files
file_to_loud = os.path.join("Resources" , "election_data.csv")
data = csv.reader(file_to_loud)
total_vote = 0
candidate_uniqname = []
Voter_ID = []
county = []
clean_data = []
candidate_name = []
candidate_vote_count = []


with open(file_to_loud) as poll_data:
    reader = csv.reader(poll_data)
    header = next(reader)
    

    for row in reader:
        total_vote = total_vote + 1
        candidate_name = row[2] 
        #candidate_name.append(row[2])
        if candidate_name not in candidate_uniqname:
            candidate_uniqname.append(candidate_name)
    
    print(candidate_uniqname)
    

    
    