import os
import csv

csvpath = os.path.join('election_data.csv')

# initialize variables for use to get the final results
total_votes = 0
candidates_with_votes = {}

# open the CSV file in the same directory as the code
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader) # store the header: ['Voter ID', 'County', 'Candidate']

    # iterating through each row...
    for row in csvreader:
        candidate = row[2]
        if candidate:
            # if there's a candidate in the row, increment the total number of votes
            total_votes = total_votes + 1
            # check if the candidate exists in our dictionary to figure out the number of votes they have
            num_votes_of_candidate = candidates_with_votes.get(candidate)
            if (num_votes_of_candidate):
                candidates_with_votes[candidate] = num_votes_of_candidate + 1
            else:
                candidates_with_votes[candidate] = 1    # if the candidate does not exist in the dictionary, then just default to one vote

output_file = 'output.txt'

# open the output file for writing
with open(output_file, 'w') as text:
    print('Election Results')
    print('-------------------------')
    print(f'Total Votes: {total_votes}')
    print('-------------------------')
    text.write('Election Results\n')
    text.write('-------------------------\n')
    text.write(f'Total Votes: {total_votes}\n')
    text.write(f'-------------------------\n')
    # iterate through all of the winners to see if their number of votes is the highest
    winner = ''
    for possible_winner in candidates_with_votes:
        final_votes_of_candidate = candidates_with_votes[possible_winner]
        percentage = (final_votes_of_candidate / total_votes) * 100 # calculate the candidates percentage of votes
        percentage_str = f"{percentage:.3f}"    # format the percentage with three decimal points
        print(f'{possible_winner}: {percentage_str}% ({final_votes_of_candidate})')
        text.write(f'{possible_winner}: {percentage_str}% ({final_votes_of_candidate})\n')
        if winner == '':
            winner = possible_winner    # default to the first candidate if there is no winner yet
        elif final_votes_of_candidate > candidates_with_votes[possible_winner]:
            winner = possible_winner
    print('-------------------------')
    print(f'Winner: {winner}')
    print('-------------------------')
    text.write(f'-------------------------\n')
    text.write(f'Winner: {winner}\n')
    text.write(f'-------------------------\n')
