# Dependencies

import os
import csv


#Initalize values

count = 0
total = 0
first = 0
second = 0

# Create Dictionaries
change = []
month = []


#Load File
budget_csv = os.path.join("..","Resources", "budget_data.csv")

#Read File
with open (budget_csv) as csv_file:

    csv_reader = csv.reader(csv_file,delimiter = ",")

    #Read Header

    header_row = next(csv_file)

    #For Loop
    for row in csv_reader:

        count = count + 1

        month.append(row)
        
        total +=(int(row[1]))

        first = int(row[1])
        
        change.append(first - second)

        second = int(row[1])
   
    #Calculate Average and remove first value from calculation
    averagechange = (sum(change)-1088983) / (len(change)-1)

    #Define Max Change
    largest = max(change)

    #Define Min Change
    smallest = min(change)

#Print results to terminal

print("Financial Analysis")

print("-----------------------------------------------")

print("Total months:" + str(count))

print("Total: $" + str(total))

print("Average Change:" + str(round(averagechange,2)))

print("Greatest Increase in Profits:" + "blah" +" ($" + str(largest)+")")

print("Greatest Decrease in Profits:" + "blah" +" ($" + str(smallest)+")")

#Print results to File

txtpath = os.path.join("..","Analysis","Financials.txt")    

with open(txtpath, "w") as txtfile:

    txtfile.write("Financial Analysis")
    txtfile.write('\n')
    txtfile.write("-----------------------------------------------")
    txtfile.write('\n')
    txtfile.write("Total months:" + str(count))
    txtfile.write('\n')
    txtfile.write("Total: $" + str(total))
    txtfile.write('\n')
    txtfile.write("Average Change:" + str(round(averagechange,2)))
    txtfile.write('\n')
    txtfile.write("Greatest Increase in Profits:" + "blah" +" ($" + str(largest)+")")
    txtfile.write('\n')
    txtfile.write("Greatest Decrease in Profits:" + "blah" +" ($" + str(smallest)+")")


