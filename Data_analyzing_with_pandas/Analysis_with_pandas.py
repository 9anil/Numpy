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
#print(country_data.life_expectancy.plot())
#print(country_data.continent.sum())
# Number of countries contain in dataframe
print(country_data.shape)
numbers_of_countries=pd.unique(country_data.location)
print("Number of countries is {}".format(len(numbers_of_countries)))
print(pd.value_counts(country_data.location))
# List of continent
print(pd.unique(country_data.continent))
# Total population of all the countries listed in this dataset
total_population=country_data.population.sum()
print("Total population is {}".format(total_population))
# Overall lief expectancy across in the world
overall_expectancy=country_data.life_expectancy.sum()/len(country_data.life_expectancy)
print(len(country_data.life_expectancy))
print("Over all lief expectancy is {}".format(overall_expectancy))
#create a dataframe containing 10 countries with highest population
highest_population=country_data.sort_values('population',ascending=False).head(10)
print(highest_population)
# Add a new column to record the overall GDP per countries(product of population and per capita GDP)
country_data['GDP']=country_data.population*country_data.gdp_per_capita
print(country_data)
# Create a dataframe that counts the number countries in each continent
country_counts=country_data.groupby('continent')[['location']].count()
print(country_counts)
# create a dataframe showing the total population of each continent.
population_in_continent=country_data.groupby('continent')[['population']].sum()
print(population_in_continent)
covid_data=pd.read_csv('covid_location.csv')
print(covid_data)
# Count the number of countries for which the total_tests data is missing.
missing_test=covid_data[covid_data.total_tests.isna()]
print(missing_test)
print("Number of countries for which total test data missing is {}".format(len(missing_test)))
# Merge countries_data with covid_data on the location column.
merge_data=country_data.merge(covid_data,on='location')
print(merge_data)
# Add columns tests_per_million, cases_per_million and deaths_per_million into covid_location data.
merge_data['tests_per_million']=merge_data.total_tests*1e6/merge_data.population
merge_data['cases_per_million']=merge_data.total_cases*1e6/merge_data.population
merge_data['deaths_per_million']=merge_data.total_deaths*1e6/merge_data.population
print(merge_data)
# Create a dataframe with 10 countries that have the highest number of tests per million people.
highest_test=merge_data.sort_values('tests_per_million',ascending=False).head(50)
print(highest_test)
# Create a dataframe with 10 countries that have the highest number of positive cases per million people.
merge_data['positive_cases']=(merge_data.total_cases/merge_data.total_tests)*1e6
highest_positive_cases=merge_data.sort_values('positive_cases',ascending=False).head(10)
print(highest_positive_cases)
# Create a dataframe with 10 countries that have the highest number of deaths cases per million people?
print(merge_data.sort_values('deaths_per_million', ascending=False).head(10))
#  Count number of countries that feature in both the lists of "highest number of tests per million" and "highest number of cases per million".
highest_cases=merge_data.sort_values('cases_per_million',ascending=False).head(50)
print(highest_cases)
check=((highest_test['location'].isin(highest_cases['location']))==True)
from IPython.display import display
with pd.option_context('display.max_row',100):
    display(check)
print(check)
#check.to_csv("check.csv")