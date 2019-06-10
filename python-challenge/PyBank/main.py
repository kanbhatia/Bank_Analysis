import csv
import os
import statistics as st


csvpath = os.path.join(".","budget_data.csv")



Date = []
Profit_Loss = []
Average = 0
with open (csvpath, "r", newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #Skip the Header
    next(csvreader,None)

    for row in csvreader:
        Date.append(row [0])
        Profit_Loss.append(int(row[1]))
    
    Total_months = len(Date)
    Total_Profits = sum(Profit_Loss)
    Greatest_Increase = max(Profit_Loss)
    Greatest_decrease = min(Profit_Loss)

    #Dates
    Date_increase = Date[Profit_Loss.index(Greatest_Increase)]    
    Date_decrease = Date[Profit_Loss.index(Greatest_decrease)]

    #Average
    for i in range(len(Profit_Loss)):
        if i != 0:
            Average += (Profit_Loss[i] - Profit_Loss[i-1])

    
    # Print Output
    print ("Financial Analysis")
    print ("--------------------------")
    print ("Total Months: " +str(Total_months))
    print ("Total: $" + str(Total_Profits))
    print ("Average Change: $%.2f" % float(Average/(len(Profit_Loss)-1)))
    print (f"Greatest Increase in profits: {Date_increase} (${Greatest_Increase})")
    print (f"Greatest Decrease in profits: {Date_decrease} (${Greatest_decrease})")

    #Save info in output file
    #create file
    txtfile = open("budget_output.txt","w")
    txtfile.write ("Financial Analysis\n")
    txtfile.write ("--------------------------\n")
    txtfile.write ("Total Months: " +str(Total_months)+ "\n")
    txtfile.write ("Total: $" + str(Total_Profits)+"\n")
    txtfile.write ("Average Change: $%.2f\n" % float(Average/(len(Profit_Loss)-1)))
    txtfile.write (f"Greatest Increase in profits: {Date_increase} (${Greatest_Increase})\n")
    txtfile.write (f"Greatest Decrease in profits: {Date_decrease} (${Greatest_decrease})")
    #Close file
    txtfile.close()