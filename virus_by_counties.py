import pandas as pd
import numpy as np

my_df = pd.read_csv("us-counties.csv")

state = str(input("What state would you like to consult? Example: Washington \n").lower().capitalize())
county = str(input("Enter county (insert all to remove filter) \n").lower().capitalize())

while True:
    try:
        if state == "" or county == "":
            print("The values you entered were not valid. Try again")
        else:
            new_df =  my_df[my_df['state'] == state]
            if county != "All":
                new_df = new_df[new_df['county'] == county]

                tot_cases = new_df['cases'].value_counts().sum()
                tot_deaths = new_df['deaths'].value_counts().sum()
                break
    except Exception as e:
        print("Exception occurred: {}".format(e))
        break

print("Last update in {} {}: ".format(state,county))
print("Total cases: {}".format(tot_cases))
print("Total deaths: {}".format(tot_deaths))
