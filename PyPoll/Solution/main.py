#Dependencies

import os
import csv


# Load file
file_to_load = os.path.join("..","Resources", "election_data.csv")
# Location to Save File
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Count votes.
total_votes = 0

# Dictionaries
candidate_options = []
candidate_votes = {}
countylist = []
countyvotes = {}


# initalize and store Values
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Read CSV
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read header
    header = next(reader)

    # For loop
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Candidate Name
        candidate_name = row[2]

        # Count Name
        countyname = row[1]

        # Add Candidates
        if candidate_name not in candidate_options:

            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0

        # Candidate count
        candidate_votes[candidate_name] += 1

        # Check duplicates
        if countyname not in countylist:

            countylist.append(countyname)
            countyvotes[countyname]=0

        # County Votes
        countyvotes[countyname] += 1

    # Print the final votes to terminal
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:}\n"
        f"-------------------------\n\n")
    print(election_results, end="")


    # Ending vote count
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.3f}% ({votes:})\n")

        # Print candidate count and percentage to terminal
        print(candidate_results)

        # winning candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_candidate = candidate_name
            winning_count = votes

    # Print winning candidate to terminal
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")
    print(winning_candidate_summary)


    #Print results to File

    txtpath = os.path.join("..","Analysis","Election_Results.txt")    

    with open(txtpath, "w") as txtfile:
        txtfile.write(f"\nElection Results\n")
        txtfile.write(f"-------------------------\n")
        txtfile.write(   f"Total Votes: {total_votes:}\n")
        txtfile.write(f"-------------------------\n\n")
        txtfile.write(f"{candidate_name}: {vote_percentage:.3f}% ({votes:})\n")
        txtfile.write(f"-------------------------\n")
        txtfile.write(f"Winner: {winning_candidate}\n")
        txtfile.write(f"-------------------------\n")
