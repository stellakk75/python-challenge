import os #Import os module 
import csv #Read CSV files
csv_path = os.path.join('Resources','election_data.csv') #Set path for file

#Open the file election_data.csv
with open(csv_path) as election_file:
    electionreader = csv.reader(election_file, delimiter = ',')
    #Skip reading header 
    election_header = next(electionreader)
    
    #Create empty lists
    voter = [ ]
    unique_candidates = [ ] 
    candidates = [ ] 

    #Append data to empty lists
    for row in electionreader:
        #Add each voter to the voter list 
        voter.append(row[0])
        #Count total number of votes 
        vote_count = len(voter)
        #Add each candidate vote (column 3) to candidate list 
        candidates.append(row[2])
        #Store list of unique candidates  
        if row[2] not in unique_candidates:
            unique_candidates.append(row[2])

    print(f'Election Results')
    print(f'-------------------------')
    print(f'Total Votes: {vote_count}')
    print(f'-------------------------')

    #Create list to append the total ballots per candidate 
    winner = [ ] 
    #Run a loop to count each ballot for each unique candidate 
    for name in unique_candidates:
        ballots = int(candidates.count(name))
        print(f'{name}: {"%.3f" %((ballots/vote_count)*100)}% ({(candidates.count(name))})')
        winner.append(ballots)
    print(f'-------------------------')

    #Find index of candidate with highest ballot/votes
    win_index = winner.index(int(max(winner)))
    #Compare the index with the candidates list 
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
    #Loops and counts each candidates votes and outputs in % breakdown
    for name in unique_candidates:
        vote_percentage = "%.3f" %((candidates.count(name)/vote_count)*100)
        election_writer.writerow([str(name) + ': ' + str(vote_percentage) + '%' + '(' + str(candidates.count(name)) + ')' ])      
    election_writer.writerow(['-------------------------'])
    election_writer.writerow(['Winner: ' + str(winner)])
    election_writer.writerow(['-------------------------'])
