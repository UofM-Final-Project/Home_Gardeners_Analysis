# Data Sources Notes

We can pull data from RCC-ACIS.ORG and NOAA.GOV.  We will likely only use RCC-ACIS.ORG for our final data.  The other site is a convenient way for the team to download practice data while we build out the python/pandas script to import, clean and export the weather data.

## RCC-ACIS.ORG Website - http://www.rcc-acis.org/docs_webservices.html

This has API calls for pulling station data via JSON in a geographic area.  You can limit the station list based on what they record (tempertures, percipitation, etc.).  There are very good examples of the parameters to send and example code on this page.

- **StnMeta** web services call returns metadata for a station or stations meeting the specified criteria.  FIPS Codes for 7 county metro:  [27053,27037,27019,27139,27123,27163,27003]

- **StnData** web services call returns raw or summarized climate data for a single station for a range of data.

- **MultiStnData** web services call returns data for multiple stations.  FIPS Codes for 7 county metro:  [27053,27037,27019,27139,27123,27163,27003]

### Other interesting data sources if needed

**This has daily weather csv file that can be downloaded through API
https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/readme.txt

This set of data uses county codes based on a standard format called **FIPS** - Federal Information Processing Standard. One source of FIPS data is here https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/ghcnd-stations.txt

[27053,27037,27019,27139,27123,27163,27003]

MN,27,053,Hennepin County,H1
MN,27,037,Dakota County,H1
MN,27,019,Carver County,H1
MN,27,139,Scott County,H1
MN,27,123,Ramsey County,H1
MN,27,163,Washington County,H1
MN,27,003,Anoka County,H1

