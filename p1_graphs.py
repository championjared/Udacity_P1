# -*- coding: UTF-8 -*
# File:: Udacity_P1 - p1_graphs.py
# Description::
#   This is my Udacity P1 Assignment File - Analysing NYC Subway Data
from datetime import *
from pandas import *
from ggplot import *
__author__ = 'JaredChampion'
__buildCode__ = 'Udacity_P1.p1_graphs.JaredChampion.2015.07.21.13'







############
# Variable Definitions
############
csv_path = 'turnstile_weather_v2.csv'



############
# Function definitions
############


#This function handles loading the CSV data into DataFrame
def load_weather_csv(csv_f_path):
    f = open(csv_f_path)
    csv_data = pandas.read_csv(f)

    return csv_data
# end load_weather_csv()



#This function handles plotting data from a DataFrame
def plot_data_histogram(df, filename, xvar):
    #functions
    # rain days
    #g = ggplot(df, aes(x=xvar)) + geom_histogram(fill='#2196F3', binwidth=2000) + ggtitle('NYC Hourly Ridership Rainy Days') + xlab('Entries Hourly')

    # clear days
    g = ggplot(df, aes(x=xvar)) + geom_histogram(fill='#FF9800', binwidth=75) + ggtitle('NYC Hourly Ridership Clear Days') \
        + xlab('Entries Hourly') + scale_y_continuous(limits=[0, 1100]) + scale_x_continuous(limits=[0, 15000])

#colors
    #FF9800 or
    #2196F3 bl


    ggsave(g, filename)

# end plot_data()

def f(x):
    y = x[''].split('-')
    return datetime.datetime(y[0], y[1], y[2], 0, 0)

############
#Program Logic
############

#load into dataframe
data = load_weather_csv(csv_path)

#get headers as list if needed
headers = list(data.columns.values)

data = data[data['ENTRIESn_hourly'] != 0]

rain_days = data[data['rain'] == 1]
clear_days = data[data['rain'] == 0]


# Allowed dates to even out Histogram comparison
allowed_clear = ['05-01-11',
                 '05-07-11',
                 '05-03-11',
                 '05-05-11',
                 '05-06-11',
                 '05-22-11',
                 '05-28-11',
                 '05-24-11',
                 '05-30-11',
                 '05-18-11']

#print Series(clear_days.DATEn.ravel()).unique()
clear_days = clear_days[clear_days.DATEn.isin(allowed_clear)]

# drop NaN / Reset index for histogram call
# to fix current ggplot bug
rain_days = rain_days.dropna().reset_index(drop=True)
clear_days = clear_days.dropna().reset_index(drop=True)



##rain weekdays WED;SAT;SUN;MON;TUES;FRI; MON; MON; THURS;

# #1, 2 - 3, 5, 6 ,9 , 10, 11, 12
############
# Write Histograms
############

# rain days hist save
#plot_data_histogram(rain_days, 'rain_days_blue.png', 'ENTRIESn_hourly')

# clear days hist save
plot_data_histogram(clear_days, 'clear_days_or.png', 'ENTRIESn_hourly')

#data = pandas.melt(data, id_vars=['datetime', 'ENTRIESn_hourly', 'rain'])

#data_clear['DATEn_index'] = data_clear['DATEn'].split('-')
#data_clear['DATEn_fix'] = datetime.datetime(data_clear['DATEn_index'][0], data_clear['DATEn_index'][1], data_clear['DATEn_index'][3], 0, 0)


# data['DATEn_int'] = data['datetime'].str.replace(':', '')
# data['DATEn_int'] = data['DATEn_int'].str.replace('-', '')
# data['DATEn_int'] = data['DATEn_int'].str.replace(' ', '')
# data['DATEn_int'].fillna(0)
#
# g = ggplot(data, aes(x='DATEn_int', y='ENTRIESn_hourly',  fill='weekday')) + geom_bar(color='#795548') + scale_y_continuous(limits=(100,300)) \
#     + scale_x_continuous(labels=[]) + xlab('Time (4 Hour Intervals)') + ylab('Entries per Interval') + ggtitle('Hourly Entries NYC Subway')
# ggsave(g, 'point_plot.png')
