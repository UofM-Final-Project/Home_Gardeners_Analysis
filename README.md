# Frost_Date_Analysis
Pull historical weather data, geoJSON zip code data, and elevations and pinpoint last frost dates and build a model to predict future dates possibly by weather pattern.

## Project Description
Amy inquired with a horticulturist who runs a decent sized FB group for Minnesota gardeners about what might be a topic that would be useful for home gardeners. She said that there is great debate on actual last frost dates in the region. She found no consensus amongst local experts.  We plan to pull historical weather data and observation station data to pinpoint last frost dates in order to build a model to predict future last frost dates in the region based.  We were able to find historical data available http://www.rcc-acis.org/docs_webservices.html in a JSON format.  As documented on their website, "The Applied Climate Information System (ACIS) was developed and is maintained by the NOAA Regional Climate Centers (RCCs). It was designed to manage the complex flow of information from climate data collectors to the end users of climate data information. The main purpose of ACIS is to alleviate the burden of climate information management for people who use climate information to make management decisions."  

### Questions To Answer
- What has been the historical average last frost date?
- Is there an accurate way to predict the last frost date?
- Do previous temperatures and/or precipitation levels have an impact on last frost date in the spring?

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
