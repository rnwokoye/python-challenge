## PyPolling Data
import os
import csv
from collections import Counter


csv_polls = os.path.join('Resources', 'election_data.csv')
csv_polls_writepath = os.path.join('analysis', 'polls_file.csv')

with open(csv_polls) as poll_file:
    csvpoll_reader = csv.reader(poll_file, delimiter=',')
    
    
    # Remove header row
    header = next(csvpoll_reader)
    
    
    # Set Variables
    total_votes = []
    candidates = []
    list_of_candidates = []
    vote_counter = []
    
    for row in csvpoll_reader:
        total_votes.append([row[0], row[2]])
        vote_counter.append(row[2])
        
        
        if row[2] not in candidates:
            candidates.append(row[2])
            
    # Print Total votes Cast
    Total_votes = (len(total_votes))
    AllCandidates = candidates
    
    # Use counter module to count Candidate votes
    Candidate_Totals = Counter(vote_counter)
    
    # Create Dictionary Scorecard
    ScoreCard = {}
    ScoreCard['Title'] = 'Election Results'
    ScoreCard['Total Votes'] = f'Total Votes: {len(total_votes)}'
    
    
    # Format ScoreCard output
    for x, y in Candidate_Totals.items():
        
        results = (f'{x}: {(Candidate_Totals[x]/Total_votes) * 100:.3f}% ({y})')
        ScoreCard[x] = results
        
    
    ScoreCard['Winner'] = f'Winner is: {Candidate_Totals.most_common()[0][0]}'

results = []
for i in ScoreCard.values():
    results.append(i)
    
with open(csv_polls_writepath, 'w') as polls:
    polls_results = csv.writer(polls, delimiter='\n', quoting=csv.QUOTE_MINIMAL)
    polls_results.writerow(results)

# Print results to terminal
for i in results:
    print(i)