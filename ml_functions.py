'''
Functions for Chicago Crime Data Analysis.

Si Young Byun
'''

from sodapy import Socrata
import pandas as pd
import geopandas as gpd
import requests
import json
import matplotlib
import matplotlib.pyplot as plt


def get_chicago_crime_data(start_date, end_date):
    '''
    Get the crime dataset from Chicago Data Portal
    and return a dataframe for the dataset.
    Input:
    - start_date: a string for start date
    - end_date: a string for start date
    Output:
    - dataset_df: dataframe
    '''
    query = "date between '{}T00:00:00' and '{}T23:59:59'"
    socrata_domain = "data.cityofchicago.org"
    client = Socrata(socrata_domain, None)

    dataset = client.get("6zsd-86xi",
                         where=query.format(start_date, end_date),
                         limit=600000)

    dataset_df = pd.DataFrame.from_records(dataset)

    return dataset_df

def basic_crime_data_processing(df):
    '''
    A simple dataset preprocessor. Drops missing data for latitude, longitude,
    community area, and ward. Changes date column into datetime type and fixes
    data type for some columns.
    Input:
    - dataframe
    Output:
    - dataframe
    '''
    df = df.dropna(subset=["latitude", "longitude", "community_area", "ward"])
    df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%dT%H:%M:%S.%f")
    df["latitude"] = df["latitude"].astype(float)
    df["longitude"] = df["longitude"].astype(float)
    df["community_area"] = df["community_area"].astype(int)
    df["ward"] = df["ward"].astype(int)
    
    return df

def get_hist_for_features(df, col_name, filter_name, var_list):
    '''
    Given a dataframe, subset the dataframe using 
    col_name == filter_name and plot histograms for all variables
    in var_list.
    input:
    - df: dataframe
    - col_name: a string for column name
    - filter_name: a string for value to subset on
    - var_list: a list of variables
    Output:
    - histograms
    '''
    hist_df = df[(df[col_name] == filter_name)]
    hist_df = hist_df[var_list]
    hist_df.hist(figsize=(15, 5))

    return plt.show()

def get_plots_by_time(crime_df, crime_type):
    '''
    Given a chicago crime dataset, subset the dataset for certain crime type,
    and plot various graphs visualizing change over time.
    Input:
    crime_df: dataframe
    crime_type: str for crime type
    Output:
    - Graphs
    '''
    p_df = crime_df[(crime_df["primary_type"] == crime_type)]
    time_list = ["date", "year", "weekday"]

    for time in time_list:
        p_df.groupby(
            [time, 'primary_type']).size().unstack().plot(figsize=(13,5))
    
    return plt.show()

def get_gdf_from_geojson(url):
    '''
    Get a geopandas df from geojson url.
    Input: string for url
    Output: geopandas dataframe
    '''
    req = requests.get(url)
    data = req.json()
    data_gdf = gpd.GeoDataFrame.from_features(data['features'])

    return data_gdf
