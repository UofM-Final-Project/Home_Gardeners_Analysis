# Frost_Date_Analysis
Pull historical weather data, geoJSON zip code data, and elevations and pinpoint last frost dates and build a model to predict future dates possibly by weather pattern.

## Project Description
Amy inquired with a horticulturist who runs a decent sized FB group for Minnesota gardeners about what might be a topic that would be useful for home gardeners. She said that there is great debate on actual last frost dates in the region. She found no consensus amongst local experts.  We plan to pull historical weather data, geoJSON zip code data, and elevations and pinpoint last frost dates in order to build a model to predict future frost dates in the region and possibly by weather pattern.  We were able to find historical data available on weather.gov site in a GeoJSON format here: https://www.weather.gov/documentation/services-web-api.  The National Weather Service (NWS) API allows developers access to critical forecasts, alerts, and observations, along with other weather data. The API was designed with a cache-friendly approach that expires content based upon the information life cycle. The API is based upon of JSON-LD to promote machine data discovery.

### Questions To Answer
- What has been the historical average frost dates?
- Is there an accurate way to predict the last frost date?
- Does previous temperatures or precipitation have an impact on final frost date?

### Group Communication Protocols
- We communicated regularly using Slack and held weekly meeting via Zoom.
- We shared resources, research, code snippets and role updates via slack and github.
- We prepared project tracker to monitor completion of tasks and schedule due dates.

#### Team Roles
- Will (Square): Responsible for the repository.
- Bree (Triangle): Created a mockup of the machine learning model. Bree created a diagram that explained how it will work concurrently with the rest of the project steps.
- Chris (Circle): Created a mockup of the database with a set of sample data data. Chris ensured the database worked seamlessly with the rest of the project.
- Amy (X Role): Decided which technologies will be used for each step of the project.

## Machine Learning Model
Bree presented a provisional machine learning model that stands in for the final machine learning model and accomplished the following:
- Takes in data in from the provisional database
- Outputs label(s) for input data

## Database
Chris presented a provisional database that stands in for the final database and accomplished the following:
- Sample data that mimics the expected final database structure or schema
- Draft machine learning module is connected to the provisional database

## Technologies Overview

### Data Sources

The primary data source for the project will be historical weather data available via API in a JSON format at http://www.rcc-acis.org/docs_webservices.html.  We've prototyped a call to the MultiStnData subset and retrieved data available at https://github.com/UofM-Final-Project/Home_Gardeners_Analysis/tree/main/resources/example_data.json.

### Data Import, Processing and ML Application

We'll be utilizing several Python and several of the available packages to access, process, export and apply machine learning to our data.  The list includes but is not limited to 
 - Pandas
 - Requests
 - JSON 
 - ML modules
 - Numpy
 - Statistics
 - matplotlib
 - sqlalchemy

### Data Storage

We will be utilizing a PostgreSQL Database on AWS for data storage.  

### Presentation

We are exploring options for presentation of our data.  We will likely use JavaScript and possibly Tableau, Mapbox and Leaflet to present our data.  The JavaScript website could be hosted on GitHub if we only utilize images but we'll need to find a different host if we want to use interactive mapbox and leaflet applications. 
