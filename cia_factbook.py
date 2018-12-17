import sqlite3
import pandas as pd 

import matplotlib.pyplot as plt
import seaborn as sns

conn = sqlite3.connect('factbook.db')

print(' ')
print('General look at database')
print(' ')
q = "SELECT * FROM sqlite_master WHERE type='table';"
print(pd.read_sql_query(q, conn))

print(' ')
print('First 5 rows of facts table')
print(' ')
q2 = "SELECT * FROM facts LIMIT 5"
print(pd.read_sql_query(q2,conn))
print(' ')


#name - The name of the country.
#area - The total land and sea area of the country.
#population - The country's population.
#population_growth- The country's population growth as a percentage.
#birth_rate - The country's birth rate, or the number of births a year per 1,000 people.
#death_rate - The country's death rate, or the number of death a year per 1,000 people.
#area- The country's total area (both land and water).
#area_land - The country's land area in square kilometers.
#area_water - The country's waterarea in square kilometers.

print('SUMMARY STATISTICS')
print(' ')

print('Info about population')
print(' ')
q_min = "SELECT MIN(population) AS 'Minimum population', MAX(population) AS 'Maximum population', MIN(population_growth) as 'Minimum population growth', MAX(population_growth) AS 'Maximum population growth' FROM facts"
print(pd.read_sql_query(q_min, conn))

print(' ')
print('Check countries with population zero')
print(' ')

q_pop_zero = "SELECT name FROM facts WHERE population = 0"
print(pd.read_sql_query(q_pop_zero, conn))

print('It make sense that nobody is living in Antarctica')
print(' ')

print(' ')
print('Check countries with population 7256490011')
print(' ')

q_pop_big = "SELECT name FROM facts WHERE population = 7256490011"
print(pd.read_sql_query(q_pop_big, conn))

print(' ')
print('I am not sure if World should count as country ;)')
print(' ')

print(' ')
print('Which countries have the highest population density?')
print(' ')

q_dens = "SELECT name, CAST(population as float)/CAST(area as float) AS density FROM facts ORDER BY density DESC LIMIT 10"
print(pd.read_sql_query(q_dens, conn))

print(' ')
print('That is all')
print(' ')