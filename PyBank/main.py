def show_line():
    print(f"="*50)
def show_line2():
    print(f"~"*50)
import os
import csv

file_to_load = os.path.join("Resources" , "election_data.csv")

total_votes = 0
Candida_Name = []
candida_vote_count = []

with open(file_to_load, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csv_reader)
    for row in csv_reader:
        
        total_votes += 1
       
        candidate_in = (row[2])

        if candidate_in in Candida_Name:
            candida_index = Candida_Name.index(candidate_in)
            candida_vote_count[candida_index] = candida_vote_count[candida_index] + 1
        else:
            
            Candida_Name.append(candidate_in)
            candida_vote_count.append(1)

pct = []
win_vote = candida_vote_count[0]
max_index = 0
for x in range(len(Candida_Name)):
    
    vote_pct = round(candida_vote_count[x]/total_votes*100, 2)
    pct.append(vote_pct)
    
    if candida_vote_count[x] > win_vote:
        win_vote = candida_vote_count[x]
        max_index = x
election_winner = Candida_Name[max_index] 

show_line()
print('|                  Election Results                  |')
show_line()
print(f'Total Votes: {total_votes}')
show_line2()
for x in range(len(Candida_Name)):
    print(f'{Candida_Name[x]} : {pct[x]}% ({candida_vote_count[x]})')
show_line2()
print(f'Election winner: {election_winner.upper()}')
show_line2()


output_file = os.path.join("pypoll_election_results.txt")
with open(output_file, "w", newline="") as datafile:
    datafile.write('======================================================\n')
    datafile.write('|                  Election Results                  |\n')
    datafile.write('======================================================\n')
    datafile.write(f'Total Votes: {total_votes}\n')
    datafile.write('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    for x in range(len(Candida_Name)):
        datafile.write(f'{Candida_Name[x]} : {pct[x]}% ({candida_vote_count[x]})\n')
    datafile.write('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    datafile.write(f'Election winner: {election_winner.upper()}\n')
    datafile.write(f'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    datafile.write("---END OF REPORT---")
