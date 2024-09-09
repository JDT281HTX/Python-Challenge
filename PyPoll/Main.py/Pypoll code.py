import csv

total_votes = 0
candidates = {}
winner = ""
winner_votes = 0 
file_path = 'C:/Users/DonJa/Documents/Module 3 Challenge/PyPoll/Resources/election_data.csv' 
output_file_path = 'C:/Users/DonJa/Documents/Module 3 Challenge/Pypoll text results.txt'

with open(file_path, mode='r', newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader) 
    for row in csvreader:
        total_votes += 1  
        candidate = row[2] 
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1 
results = [
    f"Total Votes: {total_votes}",
    "-------------------------"]

for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    results.append(f"{candidate}: {percentage:.3f}% ({votes})")
    
    if votes > winner_votes:
        winner_votes = votes
        winner = candidate

results.append("-------------------------")
results.append(f"Winner: {winner}")
results.append("-------------------------")

for line in results:
    print(line)

with open(output_file_path, mode='w') as outfile:
    outfile.write("\n".join(results))
