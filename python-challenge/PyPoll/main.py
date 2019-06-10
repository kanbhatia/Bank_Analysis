#import os and csv
import os, csv

#Variables
Candidates = {}
Total_votes = 0
#Create a path for the csv file
csvpath = os.path.join(".", "election_data.csv")

#open and edit file
with open (csvpath, newline ="") as csvfile:
    csvreader = csv.reader(csvfile)

    next(csvreader)
    for row in csvreader:
        if row[2] not in Candidates.keys() and row[2] != "":
            Candidates [row[2]] = 0
        if row[2] in Candidates.keys():
            Candidates[row[2]] +=1
            Total_votes +=1
    
    #print output
    print ("Election Results\n ---------------------")
    print ("Total Votes" + str(Total_votes) + "---------------------")

    for i in range(len(Candidates)):
        print (f"{list(Candidates.keys())[i]}: {round(((list(Candidates.values())[i])*100/Total_votes),2)}% ({list(Candidates.values())[i]})")
        