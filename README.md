# Spring Last Freeze Date Analysis
Pull historical weather data, geoJSON county data, and elevations and pinpoint last freeze dates and build a model to predict future dates possibly by weather pattern.

Presentation of Project Deliverable #2 - [Last Freeze Date Analysis Google Slides](https://docs.google.com/presentation/d/1R1opOJd2KfH-3Pl5fK3_diW3ohS4WUmtNrZGHm76p1Y/edit?usp=sharing)

## Project Description
Amy inquired with a horticulturist who runs a decent sized FB group for Minnesota gardeners about what might be a topic that would be useful for home gardeners. She said that there is great debate on actual last frost dates in the region. She found no consensus amongst local experts.  We plan to pull historical weather data and observation station data to pinpoint last freeze dates in order to build a model to predict future last freeze dates in the region based.  We were able to find historical data available [here](http://www.rcc-acis.org/docs_webservices.html) in a JSON format.  As documented on their website, "The Applied Climate Information System (ACIS) was developed and is maintained by the NOAA Regional Climate Centers (RCCs). It was designed to manage the complex flow of information from climate data collectors to the end users of climate data information. The main purpose of ACIS is to alleviate the burden of climate information management for people who use climate information to make management decisions."  

### Questions To Answer
- What has been the historical average last freeze date?
- Is there an accurate way to predict the last freeze date?
- Do previous temperatures and/or precipitation levels have an impact on last freeze date in the spring?

## Data Exploration Phase
In efforts to understand the historical weather data available within the dataset and identify which values would be ideal for the Machine Learning Model, we pulled in data in JSON and CSV formats. The dataset contains daily 21 years of weather observations from the 7 counties that make up the Twin Cities metro.  After cleaning the data, we have 27 observation stations with 126,400 rows of observation data containing the following: Observation Date, Average Degrees, Maximum Degrees, Minimum Degrees, Precipitation, Snowfall and Snow depth.  We transformed and cleaned data using Python Pandas in Jupyter Notebook. We also created a Minnesota counties lookup table from a US Census CSV file to provide county names where the weather data only provided county codes.

### Detailed Source Information
**Weather Data** - Primary data source for historical data formatted in JSON retrieved via API
- Scope:  7 Minnesota Counties (“Twin Cities Metro”), January 2020 to present
- URL: http://www.rcc-acis.org/docs_webservices.html
- [Python Script for API Call](https://github.com/UofM-Final-Project/Home_Gardeners_Analysis/blob/main/scripts/rccacis_station_info_api_data_pull.ipynb)
- JSON File Retrieved - [example of subset of data](https://github.com/UofM-Final-Project/Home_Gardeners_Analysis/blob/main/resources/rcc_data.json)

**County Code Lookup** - County Code lookup file to translate county codes in weather data to a county name 
- Scope: Minnesota Counties
- URL: https://www2.census.gov/geo/docs/reference/codes/files/st27_mn_cou.txt

**County GeoJSON Boundaries** - Utilized for Flask interactive map with leaflet/mapbox
- Scope: Twin Cities Metro - 7 Counties
- URL: https://github.com/johan/world.geo.json/tree/d895dcbb562952b0a6462f4c38d9af0cd6a036d2/countries/USA/MN


#### Data Transformation 
Cleaned data with Python Pandas and Wrote Data to Postgres DB (CSV files were also written for prototyping our Dashboard in multiple technologies quickly).  View Python processing scripts [here](https://github.com/UofM-Final-Project/Home_Gardeners_Analysis/blob/main/scripts/calls_to_each_script.ipynb).

*Station Data*
1. Split the single lat/long value into separate latitude and longitude fields
2. Convert some data types 
3. Rename/reorder columns

*Observation Data*
1. Daily observations are an array in the JSON file. No date or keys were provided.   These have to be interpreted based on the API parameters we passed in.  After the API call we stored the parameters to resources/params_list.json.  We loop through the data by the date range and parse out the array into the columns based on the array we store in the params JSON file.
2. Measurements with “M” (missing) values.  We converted these to NULL values.
Measurements with “T” (trace) set to 0.
3. Drop any observations that were missing MINT (minimum temperature).  Several stations observed only precipitation data.  We removed these because temperature was needed.
4. Converted measurements to numeric.
5. We identified that some of the stations did not report every day of the year.  We have created count columns in the station/yearly calculations table so we can determine if we want to drop some of these stations from certain years or not.  We are running the machine learning and creating graphs to determine if we think this is necessary.

**Calculations**

Following our data cleaning step, we created several calculated values for dashboard charts/graphs and machine learning, and exported the data.  
- Used Python Pandas scripts to create 6 tables in PostgreSQL and export to CSV (for testing purposes)
- Tables station, observation, county_lookup have the source data plus calculated columns for ML and reporting
- Tables station_yearly, county_metrics, county_yearly_metrics are reporting data tables created from source data and calculations
- View v_days_until_freeze_calcs_0_to_180_days is a calculated dataset for ML.  Below is an image of the query for this view:

![view](https://github.com/UofM-Final-Project/Home_Gardeners_Analysis/blob/main/images/v_days_until_freeze_calcs_0_to_180_days.PNG)

**Full column descriptions of the tables and view can be found [HERE](https://github.com/UofM-Final-Project/Home_Gardeners_Analysis/blob/main/resources/column_descriptions.xlsx)**

**ERD**
![ERD](https://github.com/UofM-Final-Project/Home_Gardeners_Analysis/blob/main/images/quick_db_ERD.png)


## Description of the Analysis Phase
The analysis phase consisted of creating 6 tables and one view using PGadmin to prepare our data for the machine learning model. The tables created are described above.  The combined data was used to train and test our machine learning model.  

Using Jupyter Notebook, the data was imported, Features (X) was separated from the Target (y).  After we split our data into training and testing, we used a Logistic Regression Machine Learning Model to make predictions for the data using 1 for “Freeze” and 0 for “No Freeze”.  

Accuracy score tests was run multiple times with different iteration of the initial CSV file to find the most accurate score. Our initial accuracy score was 65% but after iterations, our model's accuracy increased to 99%. 

### Group Communication Protocols
- We communicated regularly using Slack and held weekly meeting via Zoom.
- We shared resources, research, code snippets and role updates via slack and github.
- We prepared [Project Tracker](https://docs.google.com/spreadsheets/d/1ZoLBoF6YWwwI8pchYqjiukvkFyxpKM1p/edit?usp=sharing&ouid=114381711604427366207&rtpof=true&sd=true) to monitor completion of tasks and schedule due dates.

#### Team Roles
##### Will:
- (square) Responsible for the repository.  
- (circle) Continue with analysis and created visuals to accompany the data story
##### Bree: 
- (Triangle) Created a mockup of the machine learning model. Bree created a diagram that explained how it will work concurrently with the rest of the project steps.
##### Chris:
- (Circle) Created a mockup of the database with a set of sample data data. 
- Chris ensured the database worked seamlessly with the rest of the project.
##### Amy: 
- (X Role) Decided which technologies will be used for each step of the project.
- Cleaned data from source files

## Machine Learning Model
### Description of preliminary data preprocessing 
We used the observed weather conditions from different weather stations around the twin cities.

### Description of preliminary feature engineering and preliminary feature selection, including their decision-making process
From those observations we cleaned the data to be able to plug into our models. For example, to determine the day of the year specific temperatures will occur, the date of an observation was in month/day/year format and we changed it to a numerical representation of the day of the year. In doing so alowed us to visualize how weather conditions change for specific days of the year and create a linear model to track those trends.

### Description of how data was split into training and testing sets 
To be able to classify a day with frost the observation data was used as a training dataset find patterns and develop understanding of a day with freezing condition to create frost. The test set dropped the column that categorize which day was freezing or not to see if the model was accurate.

###  Explanation of model choice
We decided to use a logistical regression model to first see if the model could classify a day with freezing conditions based on the weather features.
Next, we wanted to show how using one feature can change predicting a day of the year that will be below freezing. By using linear regression, two models were created to show two different trends based off of different features. The last model puts those two features together and uses linear regression to create a best fit line and predict the day of the year in which an average temp and minimum temp(around freezing) will occur.

### Each Model Specifics

- Linear_min_vs_avg.ipynb -> Creates two models using linear regression to show the difference between average temp and minimum temp with their corresponding day of the year.

- Linear_Predict_day.ipynb -> Creates model to try and predict the day of the year in which specfic avgerage and minimum temp take place. Since we are looking into freezing conditions, minimum temp should be around freezing temperature between 30 and 32 degrees.

- Logistic_classify_day.ipynb -> Creates model to classify a day with frost based on past weather conditions as its features.

## Technologies Overview

### Data Sources

See above for datasources. Data formats are JSON and CVS.

### Data Processing
We'll be utilizing several Python packages to access, process, export and apply machine learning to our data.  The list includes but is not limited to 
 - Pandas
 - Requests
 - JSON 
 - sklearn and other ML modules
 - Numpy
 - Statistics
 - matplotlib
 - sqlalchemy

### Data Storage

We will be utilizing a PostgreSQL Database for data storage.  

### Data Presentation

We are exploring options for presentation of our data.  We will likely use JavaScript and possibly Tableau, Mapbox and Leaflet to present our data.  The JavaScript website could be hosted on GitHub if we only utilize images but we'll need to find a different host if we want to use interactive mapbox and leaflet applications. 

## Dashboard
#### Storyboard for Dashboard
The purpose of the dashboard is to help users predict the last freeze date based on changes in temperature, precipitation, and snowfall. 
The dashboard will consist of three different areas:
- Overview of the Weather Map (Including layers for temperatures, precipitation, snowfall, and last frost date)
- Trend line showing the historical pattern of frost dates for last 21 years (including trend line for temperatures, precipitation, and snowfall)
- Correlation visual displaying the relationship or impact of temperatures/precipitation/snowfall on last frost date results (Including accuracy score, etc)
#### Description of the Dashboard Tool(s)
The main tool used to create the dashboard will be a combination of Flask, Tableau, Mapbox and Leaflet. Within Tableau we will use interactive geographical map, line charts, and correlation map to create the dashboard.
#### Description of interactive element(s)
By using Tableau and posting the dashboard on the Tableau public website, viewers can visit the url and interact with geographical map, trend lines and correlation visuals.
Users will have the capability to enter various temperatures, precipitation, and snowfall numbers to predict last frost dates for each county. 
