import os
import csv

csvpath = os.path.join('election_data.csv')

total_votes = 0
candidates_with_votes = {}

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader) #['Voter ID', 'County', 'Candidate']

    for row in csvreader:
        candidate = row[2]
        if candidate:
            total_votes = total_votes + 1
            num_votes_of_candidate = candidates_with_votes.get(candidate)
            if (num_votes_of_candidate):
                candidates_with_votes[candidate] = num_votes_of_candidate + 1
            else:
                candidates_with_votes[candidate] = 1

output_file = 'output.txt'

with open(output_file, 'w') as text:
    print('Election Results')
    print('-------------------------')
    print(f'Total Votes: {total_votes}')
    print('-------------------------')
    text.write('Election Results\n')
    text.write('-------------------------\n')
    text.write(f'Total Votes: {total_votes}\n')
    text.write(f'-------------------------\n')
    winner = ''
    for possible_winner in candidates_with_votes:
        final_votes_of_candidate = candidates_with_votes[possible_winner]
        percentage = (final_votes_of_candidate / total_votes) * 100
        percentage_str = f"{percentage:.3f}"
        print(f'{possible_winner}: {percentage_str}% ({final_votes_of_candidate})')
        text.write(f'{possible_winner}: {percentage_str}% ({final_votes_of_candidate})\n')
        if winner == '':
            winner = possible_winner
        elif final_votes_of_candidate > candidates_with_votes[possible_winner]:
            winner = possible_winner
    print('-------------------------')
    print(f'Winner: {winner}')
    print('-------------------------')
    text.write(f'-------------------------\n')
    text.write(f'Winner: {winner}\n')
    text.write(f'-------------------------\n')
