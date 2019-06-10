#import os and csv
import os, csv

#Variables
Candidates = {}
Total_votes = 0
winner = 0
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
    print ("Election Results\n---------------------")
    print ("Total Votes: " + str(Total_votes) + "\n---------------------")

    for i in range(len(Candidates)):
        print (f"{list(Candidates.keys())[i]}: {round(((list(Candidates.values())[i])*100/Total_votes),3)}% ({list(Candidates.values())[i]})")
     
        if (Candidates[f"{list(Candidates.keys())[i]}"] >winner):
            winner = Candidates[f"{list(Candidates.keys())[i]}"]
            winner_name  = list(Candidates.keys())[i]
    print ("---------------------")
    print (f"Winner: {winner_name}")
    print ("---------------------")

    #create file
    txtfile = open("election_output.txt","w")
    txtfile.write ("Election Results\n---------------------\n")
    txtfile.write ("Total Votes: " + str(Total_votes) + "\n---------------------\n")

    for i in range(len(Candidates)):
        txtfile.write (f"{list(Candidates.keys())[i]}: {round(((list(Candidates.values())[i])*100/Total_votes),3)}% ({list(Candidates.values())[i]})\n")
 
    txtfile.write ("---------------------\n")
    txtfile.write (f"Winner: {winner_name}\n")
    txtfile.write ("---------------------\n")
    #Close file
    txtfile.close()