              # WEEKLY DISEASE CASE REPORTER#
#CREATE A CLASS TO STORE DISEASE INFORMATION
class DiseaseReport:
    def __init__(self, week, disease, cases, recoveries, deaths):
      self.week = week
      self.disease = disease 
      self.cases = cases
      self.recoveries = recoveries
      self.deaths = deaths
# ENTER WEEKLY DISEASE INFORMATION
reports = [] # Create an empty list to store the report
week = input("Enter reporting week: ") # Ask the user to enter the reporting week 
disease = input("Enter disease name: ") # Ask the user to enter the disease na  
while True:# repeat until valid input is received
    try:
# Enter the number of cases, recoveries and deaths
      cases = int(input("Enter new cases: "))
      recoveries = int(input("Enter recoveries: "))
      deaths = int(input("Enter deaths: "))
      if cases < 0 or recoveries < 0 or deaths < 0: # Check that the numbers are not negative
       print("Numbers cannot be negative!")
      else:
          report = DiseaseReport(week, disease, cases, recoveries, deaths) # Create a disease report object
          reports.append(report)# Add the report to the list
          with open("disease_data.txt", "a") as file: # SAVE THE REPORT IN A TEXT FILE
             file.write(f"{week}|{disease}|{cases}|{recoveries}|{deaths}\n") # Write the report to the file
             print("\nReport saved successfully!")
      break # Break the loop if the input is valid
    except ValueError:
        print("Invalid input! Please enter numbers only.")
# 4. GENERATE THE WEEKLY REPORT
print("\n===================================")
print("       WEEKLY DISEASE REPORT")
print("===================================")
print("Reporting Week:", week)
print("Disease:", disease)
print("New Cases:", cases)
print("Recoveries:", recoveries)
print("Deaths:", deaths)
 # Calculate and display the weekly totals
print("\n---------- WEEKLY SUMMARY ----------")
total_cases = sum(r.cases for r in reports)
total_recoveries = sum(r.recoveries for r in reports)
total_deaths = sum(r.deaths for r in reports)
print("Total New Cases:", total_cases)
print("Total Recoveries:", total_recoveries)
print("Total Deaths:", total_deaths)
print("===================================")
print("       END OF WEEKLY REPORT")
print("===================================")