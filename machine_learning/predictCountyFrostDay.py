# Import our dependencies
import pandas as pd
from pathlib import Path
from datetime import datetime
from sklearn.linear_model import LinearRegression

###
# Call the predictCountyFrostDay.py passing a county_name, read in county_yearly_metrics_data.csv,
# then it will run a linear regression model making prediction, finally it would return the predict 
# last day for frost for 2023 in mm-dd-yyyy format.
# 


def frost_predict(county_name):

    # countyList = ["Hennepin County", "Carver County", "Anoka County", "Ramsey County", "Washington County", "Scott County", "Dakota County"]

    # a = True
    # # Ask user to enter county, keeps asking until valid county name is entered
    # # Need to enter "County" after the county name
    # while a:

    #     userInput = input("Enter county name to predict last freeze day for 2023. \nHennepin County,\nCarver County,\nAnoka County,\nRamsey County,\nWashington County,\nScott County, or\nDakota County")

    #     if userInput not in countyList:
    #         print("County not found, please enter correctly")
    #     else:
    #         a = False

    frostDay = runModel(county_name)

    print(f"Predicted last day of frost for {county_name} in 2023 is {frostDay}")

    return frostDay

def runModel(userInput):

    # Reads in yearly metrics csv
    # 7 total counties
    File_path = "../resources/county_yearly_metrics_data.csv"
    county_yearly_df = pd.read_csv(File_path)
    
    Frost_day_df = county_yearly_df[["county_name", "obs_year", "last_freeze_dayofyear"]].copy()
    Frost_day_df = Frost_day_df.dropna()
    Frost_day_df = Frost_day_df.reset_index(drop=True)

    # Take userInput and remove all other counties from Frost_day_df
    if userInput == "Hennepin County":
        Frost_day_df = Frost_day_df[Frost_day_df.county_name == userInput]
    elif userInput == "Carver County":
        Frost_day_df = Frost_day_df[Frost_day_df.county_name == userInput]
    elif userInput == "Anoka County":
        Frost_day_df = Frost_day_df[Frost_day_df.county_name == userInput]
    elif userInput == "Ramsey County":
        Frost_day_df = Frost_day_df[Frost_day_df.county_name == userInput]
    elif userInput == "Washington County":
        Frost_day_df = Frost_day_df[Frost_day_df.county_name == userInput]
    elif userInput == "Scott County":
        Frost_day_df = Frost_day_df[Frost_day_df.county_name == userInput]
    else:
        Frost_day_df = Frost_day_df[Frost_day_df.county_name == userInput]

    # Add features to model
    X = Frost_day_df.obs_year.values.reshape(-1, 1)
    y = Frost_day_df.last_freeze_dayofyear

    model = LinearRegression()
    model.fit(X, y)

    # Make prediction for 2023
    predicted_dayofyear = model.predict([[2023]])

    # Convert to int to remove brackets and use as whole number
    dayofyearInt = int(predicted_dayofyear)

    # Take int version and convert to string to be converted to date format mm-dd-yyyy
    dayofyear = str(dayofyearInt)
    # adjusting day num
    dayofyear.rjust(3 + len(dayofyear), '0')
    
    # Initialize year
    year = "2023"

    # converting to date
    dateConverted = datetime.strptime(year + "-" + dayofyear, "%Y-%j").strftime("%m-%d-%Y")

    return dateConverted

# frost_predict()
