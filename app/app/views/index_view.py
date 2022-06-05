from . import bp as app
from flask import render_template,request,redirect,url_for
from app import db
import json
from ..models.station_model import station as Station
from ..models.county_lookup_model import county_lookup as CountyLookup
from ..models.county_metrics_model import county_metrics as CountyMetrics
from ..models.county_yearly_metrics_model import county_yearly_metrics as CountyYearlyMetrics
from ..models.observation_model import observation as Observation
from ..models.station_yearly_model import station_yearly as StationYearly


import pandas as pd


@app.get('/')
def index():
    markers=[
    {
    'lat':0,
    'lon':0,
    'popup':'This is the middle of the map.'
        }
    ]
    stations = Station.query.all()
    county_lookup = CountyLookup.query.all()
    county_metrics = CountyMetrics.query.all()
    county_yearly_metrics = CountyYearlyMetrics.query.all()
    observation = Observation.query.all()
    station_yearly = StationYearly.query.all()



    stations_list = []
    county_lookup_list=[]
    county_metrics_list=[]
    county_yearly_metrics_list=[]
    observation_list=[]
    station_yearly_list=[]


    for row in stations:
        stations_list.append({
            'station_uid':row.station_uid,
            'name':row.name,
            'county':row.county,
            'state':row.state,
            'latitude':row.latitude,
            'longitude':row.longitude,
            'climdiv':row.climdiv,
            'avg_last_freeze_dayofyear':row.avg_last_freeze_dayofyear,
            'avg_last_freeze_mm_dd':row.avg_last_freeze_mm_dd,
            'median_last_freeze_dayofyear':row.median_last_freeze_dayofyear,
            'median_last_freeze_mm_dd':row.median_last_freeze_mm_dd,
            'years_included':row.years_included,
            'count_at_or_before_avg_last_freeze':row.count_at_or_before_avg_last_freeze,
            'count_later_than_avg_last_freeze':row.count_later_than_avg_last_freeze,
            'stations_yearly':row.stations_yearly,
            'observations':row.observations,
        })

    for row in county_lookup:
        county_lookup_list.append({
            'state':row.state,
            'county_code':row.county_code,
            'county_name':row.county_name,
        })
    
    for row in county_metrics:
        county_metrics_list.append({
            'county':row.county,
            'county_name':row.county_name,
            'station_count':row.station_count,
            'avg_last_freeze_dayofyear':row.avg_last_freeze_dayofyear,
            'avg_last_freeze_mm_dd':row.avg_last_freeze_mm_dd,
            'median_last_freeze_dayofyear':row.median_last_freeze_dayofyear,
            'median_last_freeze_mm_dd':row.median_last_freeze_mm_dd,
            'years_included':row.years_included,
            'count_at_or_before_avg_last_freeze':row.count_at_or_before_avg_last_freeze,
            'count_later_than_avg_last_freeze':row.count_later_than_avg_last_freeze,
        })



    for row in observation:
        observation_list.append({
            'station_uid':row.station_uid,
            'date':row.date,
            'maxt':row.maxt,
            'mint':row.mint,
            'pcpn':row.pcpn,
            'snow':row.snow,
            'snwd':row.snwd,
            'avgt':row.avgt,
            'freeze_day':row.freeze_day,
            'above_freezing':row.above_freezing,
            'obs_year':row.obs_year,
            'obs_month':row.obs_month,
            'obs_day':row.obs_day,
            'obs_dayofyear':row.obs_dayofyear,
            'maxt_7_day':row.maxt_7_day,
            'mint_7_day':row.mint_7_day,
            'avgt_7_day':row.avgt_7_day,
            'precip_7_day':row.precip_7_day,
            'obs_count_7_day':row.obs_count_7_day,
            'maxt_30_day':row.maxt_30_day,
            'mint_30_day':row.mint_30_day,
            'avgt_30_day':row.avgt_30_day,
            'precip_30_day':row.precip_30_day,
            'obs_count_30_day':row.obs_count_30_day,
        })


    for row in county_yearly_metrics:
        county_yearly_metrics_list.append({
            'county':row.county,
            'obs_year':row.obs_year,
            'county_name':row.county_name,
            'coldest_day':row.coldest_day,
            'coldest_dayofyear':row.coldest_dayofyear,
            'hottest_day':row.hottest_day,
            'hottest_dayofyear':row.hottest_dayofyear,
            'last_freeze_date':row.last_freeze_date,
            'last_freeze_dayofyear':row.last_freeze_dayofyear,
            'first_freeze_date':row.first_freeze_date,
            'first_freeze_dayofyear':row.first_freeze_dayofyear,
            'observations_recorded_april_to_may':row.observations_recorded_april_to_may,
        })
    for row in station_yearly:
        station_yearly_list.append({
            'station_uid':row.station_uid,
            'obs_year':row.obs_year,
            'coldest_day':row.coldest_day,
            'coldest_dayofyear':row.coldest_dayofyear,
            'hottest_day':row.hottest_day,
            'hottest_dayofyear':row.hottest_dayofyear,
            'last_freeze_date':row.last_freeze_date,
            'last_freeze_dayofyear':row.last_freeze_dayofyear,
            'first_freeze_date':row.first_freeze_date,
            'first_freeze_dayofyear':row.first_freeze_dayofyear,
            'observations_recorded_april_to_may':row.observations_recorded_april_to_may,
        })


    station_df = pd.DataFrame(stations_list)
    county_lookup_df = pd.DataFrame(county_lookup_list)
    county_metrics_df = pd.DataFrame(county_metrics_list)
    county_yearly_metrics_df = pd.DataFrame(county_yearly_metrics_list)
    observation_df = pd.DataFrame(observation_list)
    station_yearly_df = pd.DataFrame(station_yearly_list)

    # print(station_df)
    # print(county_lookup_df)
    # print(county_metrics_df)
    # print(county_yearly_metrics_df)
    # print(observation_df)
    # print(station_yearly_df)


    

    data = [
        ['Year','State','Freeze'],
        ['2017','Hennepin','150'],
        ['2018','Ramssey','120'],
        ['2019','Scott','110'],
        ['2020','Washington','200']
    ]
    return render_template('dashboard.html',data=json.dumps(data),pannel = "Dashboard Mockup",stations=stations,markers=markers )