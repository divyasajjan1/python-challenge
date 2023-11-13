import os
import csv

#Define csv file path
pypollcsv = os.path.join('Resources','election_data.csv')

#initialize variables
total_votes = 0
candidates_list = []
candidate_votes={}
winner = ""
percent_votes = 0
votes_list = []

#Read the csv file
with open(pypollcsv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #Skip the csv header
    csv_header = next(csvreader)

    #Iterate over each row
    for row in csvreader:
        #Get the candidate data from the current row
        candidate = row[2]

        #Count total votes
        total_votes += 1

        #Count candidate votes and add to a dictionary and make a list of candidates
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidates_list.append(candidate)
            candidate_votes[candidate] = 1

    #Print results to the terminal
    print('Election Results')
    print('-------------------------')
    print(f'Total Votes: {total_votes}')
    print('-------------------------')

    #Calculate percentage of votes for each candidate and print
    for candidate in candidates_list:
        votes = candidate_votes[candidate]
        percent_votes = round((votes/total_votes)*100, 3)

        print(f'{candidate}: {percent_votes}% ({votes})')

    #Determine the winner
    winning_votes = max(candidate_votes.values())
    for candidate in candidate_votes:
        if candidate_votes[candidate] == winning_votes:
            winner = candidate

    print('-------------------------')
    print(f'Winner: {winner}')
    print('-------------------------')

    #Export the results to a text file
    output_file = os.path.join('analysis','election_results.txt')
    with open(output_file, 'w') as textfile:
        textfile.write('Election Results\n')
        textfile.write('-------------------------\n')
        textfile.write(f'Total Votes: {total_votes}\n')
        textfile.write('-------------------------\n')
        for candidate in candidates_list:
            votes = candidate_votes[candidate]
            percent_votes = round((votes/total_votes)*100, 3)

            textfile.write(f'{candidate}: {percent_votes}% ({votes})\n')
        textfile.write('-------------------------\n')
        textfile.write(f'Winner: {winner}\n')
        textfile.write('-------------------------\n')
