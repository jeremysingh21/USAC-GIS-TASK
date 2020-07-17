#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# !pip install upgrade pandas
import pandas as pd
# !pip install sodapy
from sodapy import Socrata
# !pip install mapboxgl
from mapboxgl.utils import df_to_geojson
import requests


# In[ ]:


# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
client = Socrata("opendata.usac.org", None)
results = client.get("9s6i-myen")

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_dict(results)


# In[ ]:


# filter data to year 2018 and In Window
df_filter = results_df.loc[(results_df['funding_year']=='2018')&(results_df['is_certified_in_window']=='In Window')]
# select necessary columns
df_filter = df_filter[['epc_organization_id','application_number','org_state','funding_year',
                       'funding_request_amount','latitude','longitude']]

# recast columns since data from api returned as objects
df_filter["funding_request_amount"] = df_filter.funding_request_amount.astype(float)
df_filter["latitude"] = df_filter.latitude.astype(float)
df_filter["longitude"] = df_filter.longitude.astype(float)

# applicant level aggregation with # of applications and total funding amt
df_app = df_filter.groupby(['epc_organization_id','longitude','latitude'])                    .agg({'application_number': 'nunique', 'funding_request_amount': 'sum'})                    .reset_index()

# state level aggregation with # of applications and total funding amt
df_state = df_filter.groupby(['org_state'])                    .agg({'application_number': 'nunique', 'funding_request_amount': 'sum'})                    .reset_index()
df_app


# In[ ]:


# Load data from sample csv
# Create a geojson Feature Collection from the current dataframe
geo_app = df_to_geojson(df_app, filename='app_total.geojson',
                        properties=['epc_organization_id','funding_request_amount', 'application_number'], 
                        lat='latitude', 
                        lon='longitude', 
                        precision=5)

# download as csv and join state geometry information using QGIS before conversion to geojson
df_state.to_csv('state_total.csv')

