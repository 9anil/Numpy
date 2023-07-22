import pandas as pd
# Mearging data from multiple sources
'''To determine other metrics like test per million, cases etc.'''
'''To retrive the data from url we use urlretrieve: urlretrieve("https://gist.githubusercontent.com/aakashns/8684589ef4f266116cdce023377fc9c8/raw/99ce3826b2a9d1e6d0bde7e9e559fc8b6e9ac88b/locations.csv',
            'locations.csv')'''
country_data=pd.read_csv("country_data.csv")
print(country_data)
itly=country_data[country_data.location=='Italy']
print(itly)
print(country_data[country_data.location=='India'])
# Basic plotting with pandas
'''Typically use a library like matplotlib or seaborn to plot the graphs,
Let's plot line graph showinghow the no. of daily cases varies over time using plot method
of a pandas series.'''
print(country_data.life_expectancy.plot())