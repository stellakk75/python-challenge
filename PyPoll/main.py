import os #imports os module 
import csv #reads CSV files
csv_path = os.path.join('Resources','election_data.csv')

#opens the file election_data.csv
with open(csv_path) as election_file:
    electionreader = csv.reader(election_file, delimiter = ',')
    election_header = next(electionreader)
    
    #creates empty voter list 
    voter = [ ]
    unique_candidates = [ ] 
    candidates = [ ] 

    for row in electionreader:
        #adds each voter to the voter list 
        voter.append(row[0])
        #Counts total number of votes 
        vote_count = len(voter)
        #adds each candidate vote to candidate list 
        candidates.append(row[2])
        #Stores list of unique candidates  
        if row[2] not in unique_candidates:
            unique_candidates.append(row[2])

    print(f'Election Results')
    print(f'-------------------------')
    print(f'Total Votes: {vote_count}')
    print(f'-------------------------')

    #Creates list to append the total ballots per candidate 
    winner = [ ] 
    #Runs a loop to count each ballot for each unique candidate 
    for name in unique_candidates:
        ballots = int(candidates.count(name))
        vote_percentage = (ballots/vote_count)*100
        print(f'{name}: {"%.3f" %vote_percentage}% ({ballots})')
        winner.append(ballots)
    print(f'-------------------------')

    #Finds index of candidate with highest ballot/votes
    win_index = winner.index(int(max(winner)))
    #Compares the index with the candidates list 
    winner = candidates[win_index]
    print (f'Winner: {winner}')
    print(f'-------------------------')
 
#path for output file
output_file = os.path.join('analysis','election_analysis.txt')

with open(output_file, "w", newline="") as election:
    election_writer = csv.writer(election)
    election_writer.writerow(['Election Results'])
    election_writer.writerow(['-------------------------'])
    election_writer.writerow(['Total Votes: ' + str(vote_count)])
    election_writer.writerow(['-------------------------'])
    for name in unique_candidates:
         election_writer.writerow([str(name) + ': ' + str("%.3f" %vote_percentage) + '%' + '(' + str(ballots) + ')' ])
    election_writer.writerow(['-------------------------'])
    election_writer.writerow(['Winner: ' + str(winner)])
    election_writer.writerow(['-------------------------'])


