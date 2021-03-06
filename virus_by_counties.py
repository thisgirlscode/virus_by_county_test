import pandas as pd
import numpy as np

my_df = pd.read_csv("test_data.csv")

while True:
    print("Welcome to this exercise")

    state = str(input("What state would you like to consult? Example: Washington \n").lower().capitalize())
    county = str(input("Enter county (insert all to remove filter) \n").lower().capitalize())

    try:
        if state == "":
            print("The value you entered is valid. Try again")
        else:
            if county == "":
                print("The value you entered is valid. Try again")
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

print("\n")
print("THIS IS A COPY OF SAMPLE data and it is only for the purposes of this exercise")
print("\n")
print("Last update in {} {}: ".format(state,county))
print("Total cases: {}".format(tot_cases))
print("Total deaths: {}".format(tot_deaths))
