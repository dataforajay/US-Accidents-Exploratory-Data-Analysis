# -*- coding: utf-8 -*-
"""US Accidents (2016 - 2021).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BWjFFreNkSnz2yVUUJOpxZ_9NJCc51Lk

# US Accidents Exploratory Data Analysis
To Do - Talk about EDA
To DO - Talk about the Dataset(Source, what it contaions and how it is useful)
- Kaggle
- information about accidents
- can be useful to prevent accidents
- mention that this does not contain data about New York

- *quiet simply remove output from the pip command.*
"""

pip install opendatasets --upgrade --quiet

import opendatasets as od
download_url = 'https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents'
od.download(download_url)

data_filename = './us-accidents/US_Accidents_Dec21_updated.csv'

"""## Data Preperation and Cleaning

1. Load the file using Pandas
2. Look at the inforamtion about the data and the colums
3. Fix any missing or incorect values
"""

import pandas as pd

df = pd.read_csv(data_filename)

df.head()

df.columns

len(df.columns)

df.info()

df.describe()

"""- *Finding the total nos of Numeric Columns.*"""

numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']

numeric_df = df.select_dtypes(include=numerics)
len(numeric_df.columns)

"""- *Is there any null values.*"""

df.isna()

"""- *The total sum of per column of missing values*"""

df.isna().sum()

"""- *Percentage of missing vaules per column in descending order*"""

missing_percentages = df.isna().sum().sort_values(ascending = False) / len(df)
missing_percentages

missing_percentages[missing_percentages != 0]

type(missing_percentages)



missing_percentages[missing_percentages != 0].plot(kind = 'barh' )

"""Remove columns that you don't want to use."""



"""## Exploratory Analysis and Visuilzation.
- columns we'll analyze
1. City
2. Start Time
3. Start Lat, Start Lng
4. Temperature
5. Weather Condition


"""

df.columns

df.City

cities = df.City.unique()
len(cities)

cities_by_accident = df.City.value_counts()
cities_by_accident

cities_by_accident[:20]

type(cities_by_accident)

cities_by_accident[:20].plot(kind= 'barh')

import seaborn as sns
sns.set_style("darkgrid")

sns.histplot(cities_by_accident, log_scale=True)

"""### START TIME"""

df.Start_Time

df.Start_Time[0]

pd.to_datetime(df.Start_Time)

df.Start_Time = pd.to_datetime(df.Start_Time)

"""- *Since there are 24 hours in a day, So bins=24*"""

sns.histplot(df.Start_Time.dt.hour, bins=24)

"""- *Percentage for the date time in hour*
- *Percentage for the histplot use norm_hist=True*
"""

sns.distplot(df.Start_Time.dt.hour, bins=24, kde=False, norm_hist=True)

"""- A high percebtge of accidents occur between 3 pm to 6 pm(probably people in a hurry to get to home from work).
- Next highest percentage is 6 am to 10 am.(probably perople in hurry to get to work from home).

- *Percentage plot of datetime in dayofweek(for days in a week)*
"""

sns.distplot(df.Start_Time.dt.dayofweek, bins=7, kde=False, norm_hist=True)

"""- On week ends there are less accidents.

- *Is the distributions of accidents by hour the same on weekends as on weekdays*
"""

sundays_start_time = df.Start_Time[df.Start_Time.dt.dayofweek == 6]
sundays_start_time

sns.distplot(sundays_start_time.dt.hour, bins=24, kde=False, norm_hist=True)

"""- Here we can see a bell shaped curve. 
- Which indicates that the max no of accidents in the afternoon.

- lets see it for the months.
"""

df.Start_Time.dt.year

df_2016 = df[df.Start_Time.dt.year == 2016]
sns.distplot(df_2016.Start_Time.dt.month, bins=12, kde=False, norm_hist=True)

df_2020 = df[df.Start_Time.dt.year == 2020]
sns.distplot(df_2020.Start_Time.dt.month, bins=12, kde=False, norm_hist=True)

"""Can you explain the month_wise trend of accidents?

- Much Data is missing for 2016. May be even 2020

"""

df.columns

"""### Start Latitude and Logitude"""

df.Start_Lat

df.Start_Lng

"""- Lets do a Scatter Plot and see 10% sample points of the Latitude and Logitude.


"""

sample_df = df.sample(int(0.1*len(df)))

sns.scatterplot(x=sample_df.Start_Lng, y=sample_df.Start_Lat, size= 0.001)

import folium

lat, lng = df.Start_Lat[0], df.Start_Lng[0]
lat, lng

"""- Converting Lat and Lng into a pair of list"""

(zip(list(df.Start_Lat), list(df.Start_Lng)))

from folium.plugins import HeatMap

sample_df = df.sample(int(0.001 * len(df)))
lat_lng_pairs = list(zip(list(sample_df.Start_Lat), list(sample_df.Start_Lng)))

map = folium.Map()
HeatMap(lat_lng_pairs).add_to(map)
map



cities_by_accident[cities_by_accident == 1]









high_accident_cities = cities_by_accident[cities_by_accident >= 1000]
low_accident_cities = cities_by_accident[cities_by_accident < 1000]

len(high_accident_cities)

len(high_accident_cities)/len(cities)

sns.distplot(high_accident_cities)

sns.distplot(low_accident_cities)



'NY' in df.State





"""## Ask and answer questions

1. Are there more accidents in warmer or colder areas?
2. Which 5 states have the highest number of accidents? How about per capita?
3. Does New York show up in the data? If yes, why is the count lower if this the high. 
4. Among the top 100 cities in number of accident, which states do they belong to most frequently.
5. What time of the day are accidents most frequent in ? ANSWERED
6. Which days of the week have the week have the most accidents?
7. Which months have the most accidents?
8. What is the trends of accidents year over year(decreasing /increasing?)
9. When is the accidents per unit of the traffic the highest.









"""



"""## Summary and Conclusion 

Insights:
- NO Data from New York.
- The no of accident per city descreases exponentially.
- Less than 4.2% of cities have more than 1000 yearly accidents.
- Over 1110 cities have reportes just one accident.(need to investegate)
"""

