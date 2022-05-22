# Frost_Date_Analysis
Pull historical weather data, geoJSON zip code data, and elevations and pinpoint last frost dates and build a model to predict future dates possibly by weather pattern.

## Project Description
Amy inquired with a horticulturist who runs a decent sized FB group for Minnesota gardeners about what might be a topic that would be useful for home gardeners. She said that there is great debate on actual last frost dates in the region. She found no consensus amongst local experts.  We plan to pull historical weather data and observation station data to pinpoint last frost dates in order to build a model to predict future last frost dates in the region based.  We were able to find historical data available http://www.rcc-acis.org/docs_webservices.html in a JSON format.  As documented on their website, "The Applied Climate Information System (ACIS) was developed and is maintained by the NOAA Regional Climate Centers (RCCs). It was designed to manage the complex flow of information from climate data collectors to the end users of climate data information. The main purpose of ACIS is to alleviate the burden of climate information management for people who use climate information to make management decisions."  

### Questions To Answer
- What has been the historical average last frost date?
- Is there an accurate way to predict the last frost date?
- Do previous temperatures and/or precipitation levels have an impact on last frost date in the spring?

## Data Exploration Phase
In efforts to understand the historical weather data available within the dataset and identify which values would be ideal for the Machine Learning Model, we pulled in data in JSON and CSV formats. The dataset contains 7 counties for 21 years with 13597 rows of weather results per CSV, each containing the following: Dates, Average Degrees, Maximum Degrees, Minimum Degrees, Precipitation, Snowfall and Snow depth.  We transformed and cleaned data using Python in Jupyter Notebook.  
#### We created 3 main Data frames and wrote them to CSV:
- Station_Data.csv – Added columns with average freeze dates
- Station_Year_Data.csv – Table with Primary Key of Station & Year.  Completed several calculations about the year to help with Graphing/Charting.
- Observation_Data.csv – We flag if the day has freeze and if the day goes above freezing.  Separated dates into day, month, year, and day of year. 

## Description of the Analysis Phase
The analysis phase consisted of creating 2 tables using PGadmin to prepare our data for the machine learning model. The tables created are the ‘Observations’ and 'Stations'.  The combined SQL query was exported as CSV file and used to train and test our machine learning model.  

Using Jupyter Notebook, the CSV file was imported, Features (X) was separated from the Target (y).  After we split our data into training and testing, we used a Logistic Regression Machine Learning Model to make predictions for the data using 1 for “Frost” and 0 for “No Frost”.  

Accuracy score tests was ran multiple times with different iteration of the initial CSV file to find the most accurate score. Our initial accuracy score was 65% but after iterations, our model's accuracy increased to 99%. 

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

## Machine Learning Model
Bree presented a provisional machine learning model that stands in for the final machine learning model and accomplished the following:
- There are 2 .ipynb machine learning files in the machine_learning folder that will be used in predicting frost.
- These are both used as a provisional machine learning models and will be refactored as project progresses.
- Both programs read in example csv file from a resources folder to test if they are working, but can change to read in from another source.
- Used logistic regression for categorical, predicts what makes a day have frost and chance there will be a day of frost after a specific day.
- Future improvements will use linear regression to track and try to predict the last day of frost for the spring as well as combining all machine learning files into one .py file.

#### Each Program Specifics
- LogisReg_chance_day_is_frost.ipynb -> Outcome which day will have frost, 1 means there was frost 0 means no frost
- LogisReg_chance_frost_after_day.ipynb -> Outcome there is a day of frost after specific day 3/5(March 5th) per year, 1 means there was frost 0 means no frost

## Database
The schema below illustrates the anticipated shape and content of our database: 
<img width="614" alt="Screen Shot 2022-05-15 at 10 01 20 PM" src="https://user-images.githubusercontent.com/4724180/168512789-ea1bafb5-7e60-4b5f-aec8-4ee9d1b10545.png">

## Technologies Overview

### Data Sources

The primary data source for the project will be historical weather data available via API in a JSON format at http://www.rcc-acis.org/docs_webservices.html.  We've prototyped a call to the MultiStnData subset available at https://github.com/UofM-Final-Project/Home_Gardeners_Analysis/blob/main/scripts/rccacis_station_info_api_data_pull.ipynb and retrieved data available at https://github.com/UofM-Final-Project/Home_Gardeners_Analysis/tree/main/resources/example_data.json.

### Data Import, Processing and ML Application

We'll be utilizing several Python and several of the available packages to access, process, export and apply machine learning to our data.  The list includes but is not limited to 
 - Pandas
 - Requests
 - JSON 
 - sklearn and other ML modules
 - Numpy
 - Statistics
 - matplotlib
 - sqlalchemy

### Data Storage

We will be utilizing a PostgreSQL Database on AWS for data storage.  

### Presentation

We are exploring options for presentation of our data.  We will likely use JavaScript and possibly Tableau, Mapbox and Leaflet to present our data.  The JavaScript website could be hosted on GitHub if we only utilize images but we'll need to find a different host if we want to use interactive mapbox and leaflet applications. 

## Dashboard
#### Storyboard for Dashboard
The purpose of the dashboard is to help users predict the last frost date based on changes in temperature, precipitation, and snowfall. 
The dashboard will consist of three different areas:
- Overview of the Weather Map (Including layers for temperatures, precipitation, snowfall, and last frost date)
- Trend line showing the historical pattern of frost dates for last 21 years (including trend line for temperatures, precipitation, and snowfall)
- Correlation visual displaying the relationship or impact of temperatures/precipitation/snowfall on last frost date results (Including accuracy score, etc)
#### Description of the Dashboard Tool(s)
The main tool used to create the dashboard will be a combination of Flask, Tableau, Mapbox and Leaflet. Within Tableau we will use interactive geographical map, line charts, and correlation map to create the dashboard.
#### Description of interactive element(s)
By using Tableau and posting the dashboard on the Tableau public website, viewers can visit the url and interact with geographical map, trend lines and correlation visuals.
Users will have the capability to enter various temperatures, precipitation, and snowfall numbers to predict last frost dates for each county. 
